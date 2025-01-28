from wcferry import Wcf
import json
import time
import random


def main():
    global index
    wcf = Wcf()
    lgin = wcf.is_login()
    print(lgin)

    # 获取联系人列表
    gtcontacts = wcf.get_contacts()
    with open("gtcontacts.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(gtcontacts, indent=4, ensure_ascii=False))
    # 过滤联系人，去除公众号，群聊等
    filter_contacts('gtcontacts.json', 'gtcontacts_wxid.json')
    # 转为联系人字典 微信号:昵称 格式
    contacts_dict('gtcontacts_wxid.json', 'gt.json')

    # 读取联系人字典
    with open('gt.json', 'r', encoding='utf-8') as f:
        contacts = json.load(f)
        # 遍历发送祝福语
        # value:昵称 key:微信id
        for key, value in contacts.items():
            wishesTXT = wishesSentence()
            print(f'🚀{value}🚀 {wishesTXT} wxid:{key}')
            wcf.send_text(f'🚀{value}🚀 {wishesTXT}', key)
            print(f'已发送：🚀{value}🚀 {wishesTXT} wxid:{key} sent!')
            print(f'\n\n\n')
            time.sleep(3)

# 读取祝福语文件并随机抽取一句
def wishesSentence():
    try:
        with open('wishes.txt', 'r', encoding='utf-8') as file:
            wishes = [line.strip() for line in file if line.strip()]
            
        if not wishes:
            raise ValueError("祝福语文件为空或只包含空行")
            
        return random.choice(wishes)
        
    except FileNotFoundError:
        raise FileNotFoundError("wishes.txt文件未找到")
    except Exception as e:
        raise RuntimeError(f"读取文件时发生错误: {str(e)}")
    

# 保留wxid开头的联系人
def filter_contacts(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        contacts = json.load(f)
    
    filtered_contacts = [contact for contact in contacts if contact['wxid'].startswith('wxid_')]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_contacts, f, ensure_ascii=False, indent=4)

# 联系人字典
def contacts_dict(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        contacts = json.load(f)
    
    contacts_dict = {}
    for contact in contacts:
        contacts_dict[contact['wxid']] = contact['name']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(contacts_dict, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
