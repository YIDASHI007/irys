#!/usr/bin/env python3
"""
CF Clearance Scraper 网络访问测试脚本
测试服务是否可以通过网络正常访问和使用
"""

import requests
import json
import time
import sys
import socket
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

class NetworkServiceTester:
    def __init__(self, host="0.0.0.0", port=3000):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        self.session = requests.Session()
        self.results = []
        
    def print_result(self, test_name, success, message="", data=None):
        status = "✓ 通过" if success else "✗ 失败"
        color = "\033[92m" if success else "\033[91m"
        reset = "\033[0m"
        
        print(f"{color}{status} {test_name}{reset}")
        if message:
            print(f"   信息: {message}")
        if data:
            if isinstance(data, dict) or isinstance(data, list):
                data_str = json.dumps(data, indent=2, ensure_ascii=False)
                if len(data_str) > 200:
                    data_str = data_str[:200] + "..."
            else:
                data_str = str(data)
                if len(data_str) > 200:
                    data_str = data_str[:200] + "..."
            print(f"   数据: {data_str}")
        
        self.results.append({
            "test": test_name,
            "success": success,
            "message": message,
            "data": data
        })
    
    def get_local_ip(self):
        """获取本机IP地址"""
        try:
            # 创建一个临时连接来获取本地IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def test_network_connectivity(self):
        """测试网络连通性"""
        # 测试多个可能的访问地址
        test_addresses = [
            f"http://{self.host}:{self.port}",
            f"http://localhost:{self.port}",
            f"http://127.0.0.1:{self.port}",
        ]
        
        # 添加本地IP地址
        local_ip = self.get_local_ip()
        if local_ip != "127.0.0.1":
            test_addresses.append(f"http://{local_ip}:{self.port}")
        
        success_count = 0
        for address in test_addresses:
            try:
                response = self.session.get(f"{address}/health", timeout=5)
                if response.status_code == 200:
                    success_count += 1
                    print(f"   {address}: 可访问")
                else:
                    print(f"   {address}: HTTP {response.status_code}")
            except Exception as e:
                print(f"   {address}: 连接失败 - {str(e)}")
        
        if success_count > 0:
            self.print_result("网络连通性", True, 
                            f"{success_count}/{len(test_addresses)} 个地址可访问")
            return True
        else:
            self.print_result("网络连通性", False, "所有地址都无法访问")
            return False
    
    def test_service_health(self):
        """测试服务健康状态"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            if response.status_code == 200:
                self.print_result("服务健康检查", True, f"服务状态: {response.text}")
                return True
            else:
                self.print_result("服务健康检查", False, 
                                f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.print_result("服务健康检查", False, f"请求错误: {str(e)}")
            return False
    
    def test_clearance_api(self):
        """测试主要的clearance API"""
        test_urls = [
            "https://nowsecure.nl",
            "https://www.cloudflare.com",
            "https://example.com"
        ]
        
        # 尝试不同的API端点
        api_endpoints = ["/v1", "/api", "/get", "/solve"]
        
        for endpoint in api_endpoints:
            for url in test_urls:
                try:
                    print(f"🔍 测试 {endpoint} 端点，目标: {url}")
                    
                    payload = {
                        "url": url,
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                    }
                    
                    response = self.session.post(
                        f"{self.base_url}{endpoint}",
                        json=payload,
                        timeout=60
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        if "userAgent" in result and "cookies" in result:
                            self.print_result("Clearance API", True,
                                            f"成功通过 {endpoint} 获取 {url} 的clearance",
                                            {"cookies_count": len(result.get("cookies", {})),
                                             "userAgent": result.get("userAgent", "")})
                            return True
                        else:
                            self.print_result("Clearance API", True,
                                            f"端点 {endpoint} 响应正常但格式不标准",
                                            result)
                            return True
                    elif response.status_code == 404:
                        continue  # 尝试下一个端点
                    else:
                        print(f"   HTTP {response.status_code}: {response.text}")
                        
                except Exception as e:
                    print(f"   错误: {str(e)}")
                    continue
        
        self.print_result("Clearance API", False, "所有API端点测试失败")
        return False
    
    def test_concurrent_requests(self, num_requests=3):
        """测试并发请求处理能力"""
        print(f"🧪 测试 {num_requests} 个并发请求...")
        
        def make_request(request_id):
            try:
                payload = {
                    "url": "https://example.com",
                    "testId": request_id
                }
                response = self.session.post(
                    f"{self.base_url}/v1",
                    json=payload,
                    timeout=30
                )
                return request_id, response.status_code == 200, response.status_code
            except Exception as e:
                return request_id, False, str(e)
        
        successful_requests = 0
        results = []
        
        with ThreadPoolExecutor(max_workers=num_requests) as executor:
            futures = [executor.submit(make_request, i) for i in range(num_requests)]
            for future in as_completed(futures):
                request_id, success, status = future.result()
                results.append((request_id, success, status))
                if success:
                    successful_requests += 1
        
        success_rate = successful_requests / num_requests
        if success_rate >= 0.7:  # 70%成功率视为通过
            self.print_result("并发请求测试", True,
                            f"并发处理成功: {successful_requests}/{num_requests} 个请求",
                            {"成功率": f"{success_rate:.1%}"})
            return True
        else:
            self.print_result("并发请求测试", False,
                            f"并发处理能力不足: {successful_requests}/{num_requests} 个请求",
                            {"成功率": f"{success_rate:.1%}"})
            return False
    
    def test_response_time(self):
        """测试响应时间"""
        test_urls = [
            "https://example.com",
            "https://httpbin.org/ip"
        ]
        
        total_time = 0
        successful_tests = 0
        
        for url in test_urls:
            try:
                start_time = time.time()
                payload = {"url": url}
                response = self.session.post(
                    f"{self.base_url}/v1",
                    json=payload,
                    timeout=60
                )
                end_time = time.time()
                
                if response.status_code == 200:
                    response_time = end_time - start_time
                    total_time += response_time
                    successful_tests += 1
                    print(f"   {url}: {response_time:.2f}秒")
                else:
                    print(f"   {url}: 失败 (HTTP {response.status_code})")
            except Exception as e:
                print(f"   {url}: 错误 - {str(e)}")
        
        if successful_tests > 0:
            avg_time = total_time / successful_tests
            self.print_result("响应时间测试", True,
                            f"平均响应时间: {avg_time:.2f}秒",
                            {"测试数量": successful_tests, "平均时间": f"{avg_time:.2f}秒"})
            return avg_time < 30  # 平均响应时间小于30秒视为通过
        else:
            self.print_result("响应时间测试", False, "所有测试都失败")
            return False
    
    def test_error_handling(self):
        """测试错误处理能力"""
        invalid_payloads = [
            {},  # 空负载
            {"invalid": "data"},  # 无效字段
            {"url": ""},  # 空URL
            {"url": "not-a-valid-url"},  # 无效URL格式
        ]
        
        error_handled = False
        
        for i, payload in enumerate(invalid_payloads):
            try:
                response = self.session.post(
                    f"{self.base_url}/v1",
                    json=payload,
                    timeout=10
                )
                
                # 检查是否返回了适当的错误状态码
                if response.status_code in [400, 422, 500]:
                    error_handled = True
                    print(f"   无效负载 {i+1}: 正确返回 HTTP {response.status_code}")
                else:
                    print(f"   无效负载 {i+1}: 返回 HTTP {response.status_code} (期望错误码)")
                    
            except Exception as e:
                print(f"   无效负载 {i+1}: 请求异常 - {str(e)}")
        
        if error_handled:
            self.print_result("错误处理测试", True, "服务能够正确处理无效请求")
            return True
        else:
            self.print_result("错误处理测试", False, "服务错误处理能力不足")
            return False
    
    def test_endpoint_discovery(self):
        """发现可用的API端点"""
        print("🔍 发现可用的API端点...")
        
        common_endpoints = [
            "/", "/health", "/status", "/v1", "/v2", "/api", "/api/v1",
            "/browser/status", "/stats", "/info", "/metrics",
            "/get", "/solve", "/clearance", "/turnstile", "/captcha"
        ]
        
        discovered = []
        
        for endpoint in common_endpoints:
            for method in ["GET", "POST"]:
                try:
                    if method == "GET":
                        response = self.session.get(f"{self.base_url}{endpoint}", timeout=5)
                    else:
                        # 对于POST请求，发送一个简单的测试负载
                        response = self.session.post(
                            f"{self.base_url}{endpoint}", 
                            json={"test": True},
                            timeout=5
                        )
                    
                    if response.status_code != 404:
                        content_type = response.headers.get("content-type", "unknown")
                        discovered.append({
                            "endpoint": endpoint,
                            "method": method,
                            "status": response.status_code,
                            "type": content_type,
                            "size": len(response.content)
                        })
                        print(f"   {method} {endpoint} - HTTP {response.status_code}")
                        
                except Exception as e:
                    pass
        
        if discovered:
            self.print_result("端点发现", True, f"发现 {len(discovered)} 个可用端点", discovered)
            return True
        else:
            self.print_result("端点发现", False, "未发现任何可用端点")
            return False
    
    def run_comprehensive_test(self):
        """运行全面测试"""
        print(f"\n🎯 CF Clearance Scraper 网络访问测试")
        print(f"📍 目标: {self.base_url}")
        print("=" * 60)
        
        # 获取并显示本地IP信息
        local_ip = self.get_local_ip()
        print(f"🌐 本地IP地址: {local_ip}")
        print(f"🔗 网络访问地址: http://{local_ip}:{self.port}")
        print(f"🔗 外部访问地址: http://{self.host}:{self.port}")
        
        # 运行测试
        tests = [
            ("网络连通性", self.test_network_connectivity),
            ("服务健康检查", self.test_service_health),
            ("端点发现", self.test_endpoint_discovery),
            ("Clearance API", self.test_clearance_api),
            ("响应时间", self.test_response_time),
            ("并发请求", lambda: self.test_concurrent_requests(3)),
            ("错误处理", self.test_error_handling),
        ]
        
        for test_name, test_func in tests:
            if not test_func():
                # 如果网络连通性测试失败，停止后续测试
                if test_name == "网络连通性":
                    print("❌ 网络连通性测试失败，停止测试")
                    break
        
        # 统计结果
        passed = sum(1 for r in self.results if r['success'])
        total = len(self.results)
        
        print("\n" + "=" * 60)
        print(f"📊 测试总结: {passed}/{total} 项测试通过")
        
        # 提供访问信息
        if passed > 0:
            print(f"\n🌐 服务访问信息:")
            print(f"   本地访问: http://localhost:{self.port}")
            print(f"   网络访问: http://{local_ip}:{self.port}")
            if self.host == "0.0.0.0":
                print(f"   外部访问: http://<你的公网IP>:{self.port} (需要端口转发)")
        
        # 提供建议
        if passed == total:
            print("\n🎉 所有测试通过！服务运行正常，可以从网络访问。")
        elif passed >= total * 0.7:
            print("\n⚠️  大部分测试通过，服务基本可用。")
            if passed < total:
                failed_tests = [r['test'] for r in self.results if not r['success']]
                print(f"   需要关注的测试: {', '.join(failed_tests)}")
        else:
            print("\n❌ 多数测试失败，服务可能存在问题。")
        
        return passed >= total * 0.7  # 70%通过率视为成功

def main():
    # 默认使用0.0.0.0作为主机，以便测试网络访问
    host = "0.0.0.0"
    port = 3000
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    
    tester = NetworkServiceTester(host, port)
    success = tester.run_comprehensive_test()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()