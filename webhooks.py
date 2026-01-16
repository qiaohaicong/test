from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    all_files = set()
    
    if data.get('object_kind') == 'push':
        for commit in data.get('commits', []):
            # 汇总新增、修改和删除的文件
            all_files.update(commit.get('added', []))
            all_files.update(commit.get('modified', []))
            all_files.update(commit.get('removed', []))
            
    print(f"本次推送涉及的文件: {list(all_files)}")
    return "OK", 200

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
