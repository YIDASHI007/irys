#!/usr/bin/env python3
"""
接口探索脚本 - 发现可用的API端点
"""

import requests
import json

def explore_endpoints(base_url):
    """探索可能的API端点"""
    endpoints = [
        "/api/recognize",
        "/api/ocr",
        "/ocr",
        "/recognize",
        "/image/recognize",
        "/upload",
        "/api/upload",
        "/predict",
        "/api/predict",
        "/vision/recognize",
        "/api/vision/recognize"
    ]
    
    print("🔍 探索可用接口...")
    print("=" * 50)
    
    available_endpoints = []
    
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        try:
            # 尝试GET请求
            response = requests.get(url, timeout=5)
            print(f"GET {endpoint}: HTTP {response.status_code}")
            
            # 尝试POST请求（不带数据）
            response_post = requests.post(url, timeout=5)
            print(f"POST {endpoint}: HTTP {response_post.status_code}")
            
            if response.status_code != 404 or response_post.status_code != 404:
                available_endpoints.append((endpoint, response.status_code, response_post.status_code))
                
        except requests.exceptions.RequestException as e:
            print(f"ERROR {endpoint}: {str(e)}")
    
    return available_endpoints

def test_with_image(base_url, endpoint):
    """使用图片测试特定端点"""
    from PIL import Image, ImageDraw
    import tempfile
    import os
    
    # 创建测试图片
    temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
    image = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(image)
    draw.text((100, 100), "测试文字", fill='black')
    image.save(temp_file.name, 'JPEG')
    
    print(f"\n📸 测试端点: {endpoint}")
    
    try:
        with open(temp_file.name, 'rb') as image_file:
            files = {'image': ('test.jpg', image_file, 'image/jpeg')}
            # 同时尝试其他可能的字段名
            files_alt = {'file': ('test.jpg', image_file, 'image/jpeg')}
            
            # 测试image字段
            response = requests.post(f"{base_url}{endpoint}", files=files, timeout=10)
            print(f"使用 'image' 字段: HTTP {response.status_code}")
            if response.status_code == 200:
                print(f"响应: {response.text[:200]}")
                return True
            
            # 如果失败，尝试file字段
            image_file.seek(0)  # 重置文件指针
            response = requests.post(f"{base_url}{endpoint}", files=files_alt, timeout=10)
            print(f"使用 'file' 字段: HTTP {response.status_code}")
            if response.status_code == 200:
                print(f"响应: {response.text[:200]}")
                return True
                
    except Exception as e:
        print(f"错误: {str(e)}")
    finally:
        os.unlink(temp_file.name)
    
    return False

def main():
    base_url = "http://localhost:3000"
    
    print(f"探索服务: {base_url}")
    print("=" * 50)
    
    # 1. 首先检查服务是否在线
    try:
        health_response = requests.get(f"{base_url}/health", timeout=5)
        print(f"健康检查 (/health): HTTP {health_response.status_code}")
    except:
        print("健康检查端点不可用")
    
    # 2. 探索可能的端点
    endpoints = explore_endpoints(base_url)
    
    if endpoints:
        print(f"\n🎯 发现 {len(endpoints)} 个可能端点:")
        for endpoint, get_code, post_code in endpoints:
            print(f"  {endpoint} (GET: {get_code}, POST: {post_code})")
        
        # 3. 测试每个可能的端点
        print(f"\n🧪 开始测试端点...")
        for endpoint, _, _ in endpoints:
            if test_with_image(base_url, endpoint):
                print(f"✅ 成功! 可用端点为: {endpoint}")
                break
        else:
            print("❌ 所有端点测试失败")
    else:
        print("❌ 未发现可用端点")

if __name__ == "__main__":
    main()