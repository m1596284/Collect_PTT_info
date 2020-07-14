import sys
from PTTLibrary import PTT
import socket 



PTTBot = PTT.Library()
try:
    PTTBot.login(
        'YOUR ID',
        'YOUR PW',
        KickOtherLogin=True
    )
except PTT.Exceptions.LoginError:
    PTTBot.log('登入失敗')
    sys.exit()
except PTT.Exceptions.WrongIDorPassword:
    PTTBot.log('帳號密碼錯誤')
    sys.exit()
except PTT.Exceptions.LoginTooOften:
    PTTBot.log('請稍等一下再登入')
    sys.exit()
PTTBot.log('登入成功')
Post = PTTBot.getPost(
    'Python',
    PostIndex=7486
)
print(Post)
if Post is None:
    print('Post is None')

if Post.getDeleteStatus() != PTT.PostDeleteStatus.NotDeleted:
    if Post.getDeleteStatus() == PTT.PostDeleteStatus.ByModerator:
        print(f'[板主刪除][{Post.getAuthor()}]')
    elif Post.getDeleteStatus() == PTT.PostDeleteStatus.ByAuthor:
        print(f'[作者刪除][{Post.getAuthor()}]')
    elif Post.getDeleteStatus() == PTT.PostDeleteStatus.ByUnknow:
        print(f'[不明刪除]')

if not Post.isFormatCheck():
    print('[不合格式]')

print('Board: ' + Post.getBoard())
print('AID: ' + Post.getAID())
print('Author: ' + Post.getAuthor())
print('Date: ' + Post.getDate())
print('Title: ' + Post.getTitle())
print('Content: ' + Post.getContent())
print('Money: ' + str(Post.getMoney()))
print('URL: ' + Post.getWebUrl())
print('IP: ' + Post.getIP())
# 在文章列表上的日期
print('List Date: ' + Post.getListDate())
print('地區: ' + Post.getLocation())
# Since 0.8.19
print('文章推文數: ' + Post.getPushNumber())

PushCount = 0
BooCount = 0
ArrowCount = 0

for Push in Post.getPushList():
    if Push.getType() == PTT.PushType.Push:
        Type = '推'
        PushCount += 1
    if Push.getType() == PTT.PushType.Boo:
        Type = '噓'
        BooCount += 1
    if Push.getType() == PTT.PushType.Arrow:
        Type = '箭頭'
        ArrowCount += 1

    Author = Push.getAuthor()
    Content = Push.getContent()

    Buffer = f'{Author} 給了一個{Type} 說 {Content}'
    if Push.getIP() is not None:
        Buffer += f'來自 {Push.getIP()}'
    Buffer += f'時間是 {Push.getTime()}'
    print(Buffer)

print(f'Total {PushCount} Pushs {BooCount} Boo {ArrowCount} Arrow')
PTTBot.logout()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)    

