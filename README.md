# wishes-broadcast 🎉

## 概述
`wishes-broadcast` 是一个 Python 脚本，用于向您的微信联系人发送个性化祝福。它使用 `wcferry` 库与微信进行交互，并自动化发送消息的过程。

## 功能 ✨
- 获取微信联系人列表。
- 过滤掉公众号、群聊等非个人联系人。
- 从文本文件中读取祝福语，并向每个联系人发送随机祝福。
- 记录已发送的消息。

## 要求 📋
- Python 3.x
- [wcferry](https://github.com/lich0821/WeChatFerry) 库
- WeChat V3.9.10.27

## 安装 📦
1. 克隆仓库：
    ```sh
    git clone https://github.com/yourusername/wishes-broadcast.git
    cd wishes-broadcast
    ```

2. 安装所需依赖：
    ```sh
    pip install wcferry
    ```

## 使用方法 🚀
1. 确保您已在电脑上登录微信。

2. 在脚本所在目录准备一个名为 `wishes.txt` 的文本文件。该文件应包含每行一个祝福语。

3. 运行脚本：
    ```sh
    python wishes.py
    ```

## 脚本详情 📝
### main()
主函数初始化 `Wcf` 对象，检查用户是否已登录，获取联系人列表，过滤联系人，将其转换为字典，并向每个联系人发送祝福。

### wishesSentence()
读取 `wishes.txt` 文件并返回随机祝福语。

### filter_contacts(input_file, output_file)
过滤联系人，仅保留 `wxid` 以 'wxid_' 开头的联系人。

### contacts_dict(input_file, output_file)
将过滤后的联系人转换为以微信 ID 为键、昵称为值的字典。

## 示例 🌟
一个示例 `wishes.txt` 文件：
```
新年快乐！
祝你一切顺利！
愿你有美好的一天！
```

## 许可证 📄
此项目使用 MIT 许可证。

## 贡献 🤝
如果您有任何改进或建议，欢迎提交问题或拉取请求。

## 联系方式 📧
如有任何问题或需要支持，请发送issue。
