from flask import Flask, request, jsonify

app = Flask(__name__)

# 在 GitLab Webhook 设置页面定义的 Secret Token (选填)
GITLAB_SECRET_TOKEN = "123456"

@app.route('/webhook', methods=['POST'])
def gitlab_webhook():
    # 1. 安全验证: 检查 Token 是否匹配
    stored_token = request.headers.get('X-Gitlab-Token')
    if GITLAB_SECRET_TOKEN and stored_token != GITLAB_SECRET_TOKEN:
        return jsonify({"error": "Invalid token"}), 403

    # 2. 获取 JSON 数据
    data = request.json
    print(f"接收到的JSON数据: {data}")
    if not data:
        return jsonify({"error": "No data"}), 400

    # 3. 检查是否为 Push 事件
    if data.get('object_kind') == 'push':
        user_name = data.get('user_name')
        branch = data.get('ref').split('/')[-1]
        commits = data.get('commits', [])

        # 使用集合 set() 自动去重
        files_added = set()
        files_modified = set()
        files_removed = set()

        # 4. 遍历所有提交，提取文件列表
        for commit in commits:
            files_added.update(commit.get('added', []))
            files_modified.update(commit.get('modified', []))
            files_removed.update(commit.get('removed', []))

        # 打印结果
        print(f"--- 收到来自 {user_name} 在分支 {branch} 的推送 ---")
        print(f"新增文件: {list(files_added)}")
        print(f"修改文件: {list(files_modified)}")
        print(f"删除文件: {list(files_removed)}")

        # 你可以在这里加入你的逻辑，比如触发自动部署、发送邮件等
        return jsonify({"status": "success"}), 200

    return jsonify({"status": "ignored"}), 200

if __name__ == '__main__':
    # 这里的 5000 端口需要确保内网或外网可访问
    app.run(host='0.0.0.0', port=5000)