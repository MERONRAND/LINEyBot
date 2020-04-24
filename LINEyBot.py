from linepy import *

line = LINE()

line.log("Auth Token : \n" + str(line.authToken))

oepoll = OEPoll(line)

##名前を変える
line.profile.displayName = 'えっちなアカウント'

##ステータスメッセージを変える
line.profile.statusMessage = '誰かえっちしよー!! 童貞卒業したいなー笑笑'

line.updateProfile(line.profile)


glist = line.groups

print(len(glist))

for g in glist:
	if g == 'ca0b13774392f3c147a9e11627568f29a':
		pass
	else:
		try:
			group = line.getGroup(g)

			print(group.name)
##入ってる全グループにメッセージを送る
			a = group.name
			line.sendMessage(g,'誰かえっちしよ。')
			line.sendMessage(g,'童貞卒業したいからー笑')
			line.sendMessage(g,'おねがいーw')

##入ってる全グループのグループ名を変える
			group.name = 'エログル [見せ合いグループ]'

			line.updateGroup(group)
##入ってる全グループを退会する
			line.leaveGroup(g)

			print('成功')
		except:
			print('失敗')
