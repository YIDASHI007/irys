import tls_client
from datetime import datetime
from colorama import *
from base64 import b64encode
import asyncio, random, time, json, re, os, requests, urllib3, warnings, schedule, json,socket, time, secrets, string, pytz
import uuid
import platform
import subprocess
import hashlib

# 获取硬件码的函数
def get_hardware_id():
    """获取硬件码"""
    try:
        # 获取系统信息
        system_info = platform.system() + platform.release() + platform.machine()
        
        # 获取MAC地址
        mac = uuid.getnode()
        
        # 获取CPU信息
        cpu_info = platform.processor()
        
        # 组合信息并生成哈希
        hardware_string = f"{system_info}_{mac}_{cpu_info}"
        hardware_hash = hashlib.md5(hardware_string.encode()).hexdigest()
        
        return hardware_hash
    except Exception as e:
        print(f"获取硬件码时出错: {str(e)}")
        return "unknown_hardware_id"

# 获取公网IP地址的函数
def get_public_ip():
    """获取公网IP地址"""
    try:
        # 使用多个IP查询服务来获取公网IP
        ip_services = [
            "https://api.ipify.org",
            "https://ipinfo.io/ip",
            "https://icanhazip.com",
            "https://ident.me",
            "https://checkip.amazonaws.com"
        ]
        
        for service in ip_services:
            try:
                response = requests.get(service, timeout=5)
                if response.status_code == 200:
                    public_ip = response.text.strip()
                    # 验证IP格式
                    if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', public_ip):
                        return public_ip
            except:
                continue
        
        # 如果所有服务都失败，尝试备用方法
        try:
            response = requests.get("https://httpbin.org/ip", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get('origin', '').split(',')[0].strip()
        except:
            pass
            
        return "unknown_public_ip"
    except Exception as e:
        print(f"获取公网IP时出错: {str(e)}")
        return "unknown_public_ip"

# 版权
def show_copyright():
    """展示版权信息"""
    copyright_info = f"""{Fore.CYAN}
    *****************************************************
    *           X:https://x.com/ariel_sands_dan         *
    *           Tg:https://t.me/sands0x1                *
    *           Irys Faucet BOT Version 1.1             *
    *           Copyright (c) 2025                      *
    *           All Rights Reserved                     *
    *****************************************************
    """
    {Style.RESET_ALL}
    print(copyright_info)
    print('=' * 50)
    print(f"{Fore.GREEN}申请key: https://661100.xyz/ {Style.RESET_ALL}")
    print(f"{Fore.RED}联系Dandan: \n QQ:712987787 QQ群:1036105927 \n 电报:sands0x1 电报群:https://t.me/+fjDjBiKrzOw2NmJl \n 微信: dandan0x1{Style.RESET_ALL}")
    print('=' * 50)

class URLKeyManager:
    def __init__(self, project_id="68aecaf1b5af4c1bc528425b", base_url="https://661100.xyz/get_key.php"):
        """初始化类，设置默认的project_id和基础URL"""
        self.project_id = project_id
        self.base_url = base_url

    def generate_url(self, user_id, key):
        """根据user_id和key生成完整的URL"""
        return f"{self.base_url}?project_id={self.project_id}&user_id={user_id}&key={key}"

    def save_to_file(self, user_id, key, filename="config/credentials.txt"):
        """将user_id和key保存到txt文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"user_id: {user_id}\n")
                file.write(f"key: {key}")
            return f"数据已成功保存到 {filename}"
        except Exception as e:
            return f"保存文件时出错: {str(e)}"

    def read_from_file(self, filename="config/credentials.txt"):
        """从txt文件读取user_id和key"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                user_id = lines[0].strip().replace("user_id: ", "")
                key = lines[1].strip().replace("key: ", "")
            return user_id, key
        except FileNotFoundError:
            return None, None
        except IndexError:
            return "错误: 文件格式不正确", None
        except Exception as e:
            return f"读取文件时出错: {str(e)}", None

    def get_user_input_and_save(self, filename="config/credentials.txt"):
        """获取用户输入并保存user_id和key到文件"""
        user_id = input("请输入用户id: ")
        key = input("请输入项目key: ")
        return self.save_to_file(user_id, key, filename)

    def verify_url(self, user_id, key):
        """验证URL的返回结果"""
        url = self.generate_url(user_id, key)
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查HTTP状态码
            data = response.json()  # 解析JSON响应
            if data.get("status") == "error":
                print(f"验证失败: {data.get('message')}")
                return False
            elif data.get("status") == "success":
                print(f"验证成功: 获取到key - {data.get('key')}")
                return True
            else:
                print("未知的响应状态")
                return False
        except requests.RequestException as e:
            print(f"请求URL时出错: {str(e)}")
            return False
        except ValueError:
            print("响应不是有效的JSON格式")
            return False

    def post_user_info_to_server(self, user_id, key):
        """将用户信息POST到服务器"""
        try:
            # 硬编码服务器URL和配置
            server_url = "https://661100.xyz/user_info.php"
            timeout = 10
            
            # 获取公网IP和硬件码
            public_ip = get_public_ip()
            hardware_id = get_hardware_id()
            
            # 准备POST数据 - 同时支持新旧字段名
            post_data = {
                "user_id": user_id,
                "key": key,
                "public_ip": public_ip,
                "local_ip": public_ip,  # 兼容旧版本
                "hardware_id": hardware_id,
                "timestamp": datetime.now().isoformat(),
                "project_id": self.project_id
            }
            
            # 发送POST请求
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "KeyBot/1.0"
            }
            
            response = requests.post(server_url, json=post_data, headers=headers, timeout=timeout)
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            if result.get("status") == "success":
                print(f"{Fore.GREEN}用户信息已成功发送到服务器{Style.RESET_ALL}")
                print(f"公网IP: {public_ip}")
                print(f"硬件码: {hardware_id}")
                return True, result.get("hardware_check", {})
            else:
                print(f"{Fore.RED}服务器返回错误: {result.get('message', '未知错误')}{Style.RESET_ALL}")
                return False, None
                
        except requests.RequestException as e:
            print(f"{Fore.RED}发送POST请求时出错: {str(e)}{Style.RESET_ALL}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"{Fore.RED}服务器错误详情: {error_detail}{Style.RESET_ALL}")
                except:
                    print(f"{Fore.RED}服务器响应: {e.response.text}{Style.RESET_ALL}")
            return False, None
        except ValueError as e:
            print(f"{Fore.RED}解析服务器响应时出错: {str(e)}{Style.RESET_ALL}")
            return False, None
        except Exception as e:
            print(f"{Fore.RED}发送用户信息时出现未知错误: {str(e)}{Style.RESET_ALL}")
            return False, None

    def replace_hardware_id(self, user_id, hardware_id):
        """请求服务器替换硬件码"""
        try:
            server_url = "https://661100.xyz/replace_hardware.php"
            timeout = 10
            
            post_data = {
                "user_id": user_id,
                "hardware_id": hardware_id
            }
            
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "KeyBot/1.0"
            }
            
            response = requests.post(server_url, json=post_data, headers=headers, timeout=timeout)
            response.raise_for_status()
            
            result = response.json()
            if result.get("status") == "success":
                print(f"{Fore.GREEN}✅ {result.get('message')}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}替换次数: {result.get('replace_count')}/{result.get('max_replacements')}{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}❌ {result.get('message')}{Style.RESET_ALL}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}替换硬件码时出错: {str(e)}{Style.RESET_ALL}")
            return False

    def handle_hardware_id_change(self, user_id, hardware_check):
        """处理硬件码变化"""
        if not hardware_check:
            return True
        
        can_replace = hardware_check.get('can_replace', True)
        message = hardware_check.get('message', '')
        previous_hardware_id = hardware_check.get('previous_hardware_id')
        current_hardware_id = hardware_check.get('current_hardware_id')
        replace_count = hardware_check.get('replace_count', 0)
        max_replacements = hardware_check.get('max_replacements', 3)
        
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
        
        if not can_replace:
            if previous_hardware_id and current_hardware_id:
                print(f"{Fore.YELLOW}⚠️  检测到硬件码变化！{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}上次: {previous_hardware_id}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}当前: {current_hardware_id}{Style.RESET_ALL}")
                print(f"{Fore.RED}❌ 已达到最大替换次数({max_replacements}次)，无法继续替换{Style.RESET_ALL}")
            return False
        
        if previous_hardware_id and current_hardware_id and previous_hardware_id != current_hardware_id:
            print(f"{Fore.YELLOW}⚠️  检测到硬件码变化！{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}上次: {previous_hardware_id}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}当前: {current_hardware_id}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}当前替换次数: {replace_count}/{max_replacements}{Style.RESET_ALL}")
            
            # 询问用户是否要替换
            while True:
                choice = input(f"{Fore.CYAN}是否要替换硬件码？(y/n): {Style.RESET_ALL}").strip().lower()
                if choice in ['y', 'yes', '是']:
                    # 请求服务器替换硬件码
                    if self.replace_hardware_id(user_id, current_hardware_id):
                        return True
                    else:
                        return False
                elif choice in ['n', 'no', '否']:
                    print(f"{Fore.YELLOW}❌ 用户取消替换{Style.RESET_ALL}")
                    return False
                else:
                    print(f"{Fore.RED}请输入 y 或 n{Style.RESET_ALL}")
        
        return True

#ip池检测
class ProxyChecker:
    def __init__(self):
        """初始化，用户输入代理 IP 和端口范围"""
        self.proxy_ip = input("请输入代理 IP (例如 192.168.2.7): ").strip()
        self.start_port, self.end_port = self.get_port_range()
        self.proxy_list = []
        self.valid_proxies = []

    def get_port_range(self):
        """获取用户输入的端口范围"""
        while True:
            try:
                start_port = int(input("请输入起始端口 (如 7000): ").strip())
                end_port = int(input("请输入结束端口 (如 70100): ").strip())
                if start_port > end_port or start_port <= 0 or end_port <= 0:
                    raise ValueError("起始端口必须小于等于结束端口，且必须为正整数。")
                return start_port, end_port
            except ValueError as e:
                print(f"输入错误: {e}，请重新输入！")

    def get_random_proxies(self, count=5):
        """从端口范围内随机抽取一定数量的代理"""
        available_ports = list(range(self.start_port, self.end_port + 1))
        selected_ports = random.sample(available_ports, min(count, len(available_ports)))
        self.proxy_list = [f"{self.proxy_ip}:{port}" for port in selected_ports]

    def check_proxy(self, proxy):
        """检查 HTTP 代理是否可用"""
        print(f"正在检测代理 {proxy} 是否可用...")
        test_url = "https://www.google.com"
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        try:
            response = requests.get(test_url, proxies=proxies, timeout=5)
            if response.status_code == 200:
                print(f"代理 {proxy} 可用！")
                return True
        except requests.exceptions.RequestException:
            pass
        return False

    def filter_valid_proxies(self):
        """筛选可用的代理"""
        print("正在检测可用代理，并保存到 proxy.txt 文件...")
        self.valid_proxies = [proxy for proxy in self.proxy_list if self.check_proxy(proxy)]

    def save_proxies_to_file(self, filename="config/proxy.txt"):
        """将可用代理保存到 txt 文件"""
        if not self.valid_proxies:
            print("未找到可用代理，未生成文件。")
            return

        file_path = os.path.abspath(filename)
        print(f"保存路径: {file_path}")
        with open(filename, "w") as file:
            for proxy in self.valid_proxies:
                line = f"http://{proxy}\n"
                print(f"写入代理: {line.strip()}")
                file.write(line)

    def run(self):
        """主逻辑执行"""
        while True:
            try:
                proxy_count = int(input("请输入要随机抽取的代理数量: ").strip())
                if proxy_count <= 0:
                    raise ValueError("代理数量必须大于 0！")
                break
            except ValueError as e:
                print(f"输入错误: {e}，请重新输入！")

        self.get_random_proxies(count=proxy_count)
        self.filter_valid_proxies()
        self.save_proxies_to_file()

        if self.valid_proxies:
            print(f"已保存 {len(self.valid_proxies)} 个可用代理到 proxy.txt")
        else:
            print("没有可用代理，未生成文件。")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.2",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

user_agent = random.choice(user_agents)
wib = pytz.timezone('Asia/Shanghai')


# 配置开关
USE_API_PROXIES = False  # 设置为True从API获取代理，False从文件读取
API_PROXY_URL = ""

# 配置说明:
# USE_API_PROXIES = True:  从API动态获取代理，每次处理一个钱包获取一个新代理，失败时重试3次
# USE_API_PROXIES = False: 从proxies.txt文件读取代理，每个钱包使用对应位置的代理
# API_PROXY_URL: 代理API地址，支持多种返回格式:
#   格式1: [{"username":"...","password":"...","ip":"...","port":"..."}]
#   格式2: {"code":0,"success":"true","msg":"","data":[{"IP":"...","Port":...}]}
#   格式3: {"code":0,"data":[{"ip":"...","port":"...","username":"...","password":"..."}]}

# 加载配置文件
def load_config():
    """加载配置文件"""
    try:
        with open('config/config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"警告: 无法加载配置文件，使用默认设置: {e}")
        return {
            "captcha_wait_time": 60,
            "local_captcha_urls": ["http://192.168.2.62:3000/"],
            "site_key": "0x4AAAAAAA6vnrvBCtS4FAl-"
        }

# 加载配置
config = load_config()

def load_wallets(filename="config/address.txt"):
    """加载钱包地址列表"""
    wallets = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and line.startswith('0x'):
                    wallets.append(line)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {filename}")
        return []
    return wallets

def get_api_proxies(count=1):
    """从API获取代理列表"""
    proxies = []
    try:
        print(f"正在从API获取 {count} 个代理...")
        response = requests.get(API_PROXY_URL, timeout=30)
        
        if response.status_code == 200:
            proxy_data = response.json()
            print(f"API返回数据: {proxy_data}")
            
            # 检查不同的返回格式
            if isinstance(proxy_data, list):
                # 格式1: [{"username": "...", "password": "...", "ip": "...", "port": "..."}]
                for proxy in proxy_data:
                    proxy_config = {
                        "ip": proxy.get("ip"),
                        "port": proxy.get("port"),
                        "username": proxy.get("username"),
                        "password": proxy.get("password")
                    }
                    if all(proxy_config.values()):  # 确保所有字段都有值
                        proxies.append(proxy_config)
                        print(f"获取代理: {proxy_config['username']}@{proxy_config['ip']}:{proxy_config['port']}")
            
            elif isinstance(proxy_data, dict):
                # 格式2: {"code":0,"success":"true","msg":"","data":[{"IP":"...","Port":...}]}
                if proxy_data.get("success") == "true" and "data" in proxy_data:
                    for proxy in proxy_data["data"]:
                        proxy_config = {
                            "ip": proxy.get("IP"),
                            "port": str(proxy.get("Port")),
                            "username": "",  # 这种格式通常没有用户名密码
                            "password": ""
                        }
                        if proxy_config["ip"] and proxy_config["port"]:
                            proxies.append(proxy_config)
                            print(f"获取代理: {proxy_config['ip']}:{proxy_config['port']} (无认证)")
                
                # 格式3: {"code":0,"data":[{"ip":"...","port":"...","username":"...","password":"..."}]}
                elif proxy_data.get("code") == 0 and "data" in proxy_data:
                    for proxy in proxy_data["data"]:
                        proxy_config = {
                            "ip": proxy.get("ip"),
                            "port": proxy.get("port"),
                            "username": proxy.get("username", ""),
                            "password": proxy.get("password", "")
                        }
                        if proxy_config["ip"] and proxy_config["port"]:
                            proxies.append(proxy_config)
                            if proxy_config["username"]:
                                print(f"获取代理: {proxy_config['username']}@{proxy_config['ip']}:{proxy_config['port']}")
                            else:
                                print(f"获取代理: {proxy_config['ip']}:{proxy_config['port']} (无认证)")
            
            if not proxies:
                print("警告: 无法解析API返回的代理数据")
        else:
            print(f"API请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            
    except Exception as e:
        print(f"获取API代理失败: {e}")
    
    return proxies

def load_proxies(filename="config/proxy.txt"):
    """加载代理配置列表"""
    proxies = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        # 解析格式: http://用户名:密码@IP:端口 或 http://IP:端口
                        if line.startswith('http://'):
                            # 移除 http:// 前缀
                            url_part = line[7:]  # 移除 'http://'
                            
                            if '@' in url_part:
                                # 有认证信息的代理: http://username:password@ip:port
                                auth_part, server_part = url_part.split('@')
                                # 从右边分割，因为用户名可能包含冒号
                                if ':' in auth_part:
                                    username = auth_part.rsplit(':', 1)[0]  # 取最后一个冒号前的部分
                                    password = auth_part.rsplit(':', 1)[1]  # 取最后一个冒号后的部分
                                else:
                                    username = auth_part
                                    password = ""
                                ip, port = server_part.split(':')
                            else:
                                # 无认证信息的代理: http://ip:port
                                if ':' in url_part:
                                    ip, port = url_part.split(':')
                                    username = ""
                                    password = ""
                                else:
                                    raise ValueError("无效的代理格式")
                            
                            proxy_config = {
                                "ip": ip,
                                "port": port,
                                "username": username,
                                "password": password
                            }
                            proxies.append(proxy_config)
                        elif '@' in line:
                            # 兼容旧格式: 用户名:密码@IP:端口
                            auth_part, server_part = line.split('@')
                            # 从右边分割，因为用户名可能包含冒号
                            if ':' in auth_part:
                                username = auth_part.rsplit(':', 1)[0]  # 取最后一个冒号前的部分
                                password = auth_part.rsplit(':', 1)[1]  # 取最后一个冒号后的部分
                            else:
                                username = auth_part
                                password = ""
                            ip, port = server_part.split(':')
                            proxy_config = {
                                "ip": ip,
                                "port": port,
                                "username": username,
                                "password": password
                            }
                            proxies.append(proxy_config)
                        else:
                            print(f"警告: 跳过无效的代理配置格式: {line}")
                    except Exception as e:
                        print(f"警告: 跳过无效的代理配置: {line} - {e}")
    except FileNotFoundError:
        print(f"错误: 找不到文件 {filename}")
        return []
    return proxies

def get_turnstile_token(proxy_config=None):
    """获取 Turnstile token"""
    try:
        print("正在请求打码服务获取token...")
        # 使用配置文件中的打码服务URL
        captcha_url = config.get("local_captcha_urls", ["http://192.168.2.62:3000/"])[0]
        captcha_wait_time = config.get("captcha_wait_time", 60)
        site_key = config.get("site_key", "0x4AAAAAAA6vnrvBCtS4FAl-")
        
        print(f"打码等待时间: {captcha_wait_time} 秒")
        
        # 本地请求不使用代理
        response = requests.post(captcha_url, 
            headers={'Content-Type': 'application/json'},
            json={
                "type": "cftoken",
                "websiteUrl": "https://irys.xyz/api/faucet",
                "websiteKey": site_key
            },
            timeout=captcha_wait_time
        )
        
        result = response.json()
        if result.get('code') == 200:
            print("✅ 成功获取token")
            return result['token']
        else:
            print(f"❌ 获取token失败: {result.get('message')}")
            return None
    except Exception as e:
        print(f"❌ 获取token异常: {e}")
        return None

def claim_faucet(wallet_address, proxy_config=None, token=None):
    """领取水龙头"""
    try:
        # 获取 token（如果没有提供的话）
        if not token:
            token = get_turnstile_token(proxy_config)
            if not token:
                return False, "获取token失败"
        
        # 构造 headers
        headers = {
            'accept': '*/*',
            'accept-language': 'ja',
            'content-type': 'application/json',
            'cookie': '_ga_N7ZGKKSTW8=GS2.1.s1751726728$o1$g0$t1751726728$j60$l0$h0; _ga=GA1.1.1969698972.1751726728',
            'origin': 'https://irys.xyz',
            'priority': 'u=1, i',
            'referer': 'https://irys.xyz/faucet',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
        }
        
        # 构造请求数据
        data = {
            "captchaToken": token,
            "walletAddress": wallet_address
        }
        
        # 创建 tls_client session
        session = tls_client.Session(
            client_identifier="chrome_132",
            random_tls_extension_order=True
        )
        
        # 如果提供了代理配置，则使用代理
        if proxy_config:
            if proxy_config['username'] and proxy_config['password']:
                # 有认证信息的代理
                proxy_url = f"http://{proxy_config['username']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
            else:
                # 无认证信息的代理
                proxy_url = f"http://{proxy_config['ip']}:{proxy_config['port']}"
            session.proxies = {"http": proxy_url, "https": proxy_url}
        
        # 发送请求
        response = session.post(
            "https://irys.xyz/api/faucet",
            headers=headers,
            json=data
        )
        
        result = response.json()
        if result.get('success'):
            return True, result.get('message', '领取成功')
        else:
            return False, result.get('message', '领取失败')
            
    except Exception as e:
        return False, f"请求异常: {e}"

def process_wallet(wallet_address, proxy_config=None, token=None):
    """处理单个钱包"""
    print(f"\n开始处理钱包: {wallet_address}")
    
    success, message = claim_faucet(wallet_address, proxy_config, token)
    
    if success:
        print(f"✅ 成功: {wallet_address} - {message}")
    else:
        print(f"❌ 失败: {wallet_address} - {message}")
    
    return wallet_address, success, message

def run_main():
    """主函数"""
    print("=== Irys 批量水龙头领取工具 ===")
    
    # 加载钱包
    wallets = load_wallets()
    
    if not wallets:
        print("错误: 没有找到有效的钱包地址")
        return
    
    print(f"加载了 {len(wallets)} 个钱包地址")
    
    # 创建结果列表
    results = []
    
    # 预加载代理列表（避免重复加载）
    if not USE_API_PROXIES:
        print("正在加载代理列表...")
        proxies = load_proxies()
        print(f"加载了 {len(proxies)} 个代理")
    
    # 逐个处理钱包，每次获取一个代理
    for i, wallet in enumerate(wallets):
        print(f"\n{'='*50}")
        print(f"处理第 {i+1}/{len(wallets)} 个钱包: {wallet}")
        
        # 获取代理
        if USE_API_PROXIES:
            print("获取新的代理...")
            api_proxies = get_api_proxies(1)
            if api_proxies:
                proxy = api_proxies[0]
                print(f"使用代理: {proxy['username']}@{proxy['ip']}:{proxy['port']}")
            else:
                print("警告: 无法获取代理，将直接连接")
                proxy = None
        else:
            # 使用预加载的代理列表
            proxy = proxies[i] if i < len(proxies) else None
            if proxy:
                print(f"使用代理: {proxy['username']}@{proxy['ip']}:{proxy['port']}")
            else:
                print("警告: 没有对应的代理，将直接连接")
        
        # 处理钱包，如果失败且使用API代理，则重试
        max_retries = 3 if USE_API_PROXIES else 1
        success = False
        token = None  # 用于重试时复用token
        
        for retry in range(max_retries):
            if retry > 0:
                print(f"重试第 {retry} 次...")
                if USE_API_PROXIES:
                    print("重新获取代理...")
                    proxies = get_api_proxies(1)
                    if proxies:
                        proxy = proxies[0]
                        print(f"使用新代理: {proxy['username']}@{proxy['ip']}:{proxy['port']}")
            
            # 第一次尝试时获取token，重试时复用
            if retry == 0:
                print("首次尝试，获取打码token...")
                token = get_turnstile_token(proxy)
                if not token:
                    print("❌ 获取token失败，跳过此钱包")
                    success = False
                    message = "获取token失败"
                    break
            else:
                print(f"重试第 {retry} 次，复用之前的token...")
            
            wallet_result, success, message = process_wallet(wallet, proxy, token)
            
            if success:
                print(f"✅ 成功: {message}")
                break
            else:
                print(f"❌ 失败: {message}")
                if retry < max_retries - 1:
                    print("等待后重试...")
                    time.sleep(random.uniform(2, 5))
        
        results.append((wallet, success, message))
        
        # 添加延迟，避免请求过于频繁
        if i < len(wallets) - 1:  # 最后一个钱包不需要延迟
            delay = random.uniform(1, 5)
            print(f"等待 {delay:.1f} 秒后处理下一个钱包...")
            time.sleep(delay)
    
    # 打印统计结果
    print(f"\n{'='*50}")
    print("=== 领取结果统计 ===")
    success_count = sum(1 for _, success, _ in results if success)
    total_count = len(results)
    
    print(f"总计: {total_count}")
    print(f"成功: {success_count}")
    print(f"失败: {total_count - success_count}")
    print(f"成功率: {success_count/total_count*100:.1f}%")
    
    # 保存结果到文件
    with open('faucet_results.txt', 'w', encoding='utf-8') as f:
        f.write("=== Irys 水龙头领取结果 ===\n")
        f.write(f"时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"总计: {total_count}, 成功: {success_count}, 失败: {total_count - success_count}\n\n")
        
        for i, (wallet, success, message) in enumerate(results):
            status = "✅ 成功" if success else "❌ 失败"
            proxy_info = "API动态代理" if USE_API_PROXIES else "文件代理"
            f.write(f"{status}: {wallet} ({proxy_info}) - {message}\n")
    
    print(f"\n详细结果已保存到: faucet_results.txt")

def get_choice():
    print("\n" + "="*50)
    print(("请选择:"))
    print((f"{Fore.YELLOW}1. 生成代理池可用ip{Style.RESET_ALL}"))
    print((f"{Fore.GREEN}2. 自动完成任务{Style.RESET_ALL}"))
    print((f"{Fore.RED}3. 退出{Style.RESET_ALL}"))
    print("="*50 + "\n")

async def main():
    show_copyright()
    # 创建实例
    url_manager = URLKeyManager()
    filename = "config/credentials.txt"

    # 检查文件是否存在
    if os.path.exists(filename):
        print(f"检测到已有 {filename} 文件，尝试读取并验证...")
        user_id, key = url_manager.read_from_file()
        if user_id is None and key is None:
            print("文件不存在或为空，将要求输入新数据")
        elif isinstance(user_id, str) and "错误" in user_id:
            print(user_id)
            print("文件内容有误，将要求输入新数据")
        else:
            # 使用文件中的user_id和key进行验证
            if url_manager.verify_url(user_id, key):
                print("验证通过，继续执行后续逻辑...")
                
                # 发送用户信息到服务器
                print(f"{Fore.YELLOW}正在发送用户信息到服务器...{Style.RESET_ALL}")
                success, hardware_check = url_manager.post_user_info_to_server(user_id, key)
                
                if success and hardware_check:
                    # 检查硬件码变化
                    if not url_manager.handle_hardware_id_change(user_id, hardware_check):
                        print(f"{Fore.RED}硬件码验证失败，程序退出{Style.RESET_ALL}")
                        exit()

                get_choice()
                choice = input("输入您的选择: ").strip()
                if choice == '3':
                    print("退出...", 'info')
                elif choice == '1':
                    proxy_checker = ProxyChecker()
                    proxy_checker.run()
                elif choice == '2':
                    run_main()
                else:
                    print("看提示，不要瞎输入", 'info')

            else:
                print("验证失败，程序退出")
            exit()  # 验证完成后退出，避免重复执行

    # 如果文件不存在或读取失败，要求用户输入并保存
    result1 = url_manager.get_user_input_and_save()
    print(result1)
    
    # 读取刚保存的数据并验证
    user_id, key = url_manager.read_from_file()
    if isinstance(user_id, str) and "错误" in user_id:
        print(user_id)
    else:
        if url_manager.verify_url(user_id, key):
            print("验证通过，继续执行后续逻辑...")
            
            # 发送用户信息到服务器
            print(f"{Fore.YELLOW}正在发送用户信息到服务器...{Style.RESET_ALL}")
            success, hardware_check = url_manager.post_user_info_to_server(user_id, key)
            
            if success and hardware_check:
                # 检查硬件码变化
                if not url_manager.handle_hardware_id_change(user_id, hardware_check):
                    print(f"{Fore.RED}硬件码验证失败，程序退出{Style.RESET_ALL}")
                    exit()

            get_choice()
            choice = input("输入您的选择: ").strip()
            if choice == '3':
                print("退出...", 'info')
            elif choice == '1':
                proxy_checker = ProxyChecker()
                proxy_checker.run()
            elif choice == '2':
                run_main()
            else:
                print("看提示，不要瞎输入", 'info')
        else:
            print("验证失败，程序退出")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Irys Faucet BOT [退出]{Style.RESET_ALL}                                       "                              
        )

# if __name__ == "__main__":
#     main() 