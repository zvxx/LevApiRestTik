from flask import *
from requests import post,get
def dd(email,der):
	user = email
	try:
		url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
		headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'mid=ZHTlnQALAAFHZAE8G64BeLHXNMv6; ig_did=ACB29C06-4F89-4B7A-9D37-DC433D1E9398; ig_nrcb=1; datr=nUZ1ZAphhPG3siVLQu3QFbkq; fbm_124024574287414=base_domain=.instagram.com; csrftoken=1gI1BSItuCt7GpIB7BL3KCrapTfKligx; ds_user_id=55002803434; sessionid=55002803434%3A1m1laRSPbJaoKD%3A24%3AAYdWXJwfQhhN68tU0NIkcNODEtrIYnAgKCWPkrp3Rg; shbid="12254\05455002803434\0541717693792:01f7d20c44658c09775e0f963159681bf19a10be70bbe95b497a89f112ac2fc01ab50da0"; shbts="1686157792\05455002803434\0541717693792:01f7c175c7d720e51402db9b91b351fab16619ea5a91f0ce421bc4c9827bce14e62426c5"; fbsr_124024574287414=Z3GOftVJ7wWK4lDsT4vYGKDlPKHv5vYXWQpT8AYi130.eyJ1c2VyX2lkIjoiMTAwMDg3NjM5MTE3ODM3IiwiY29kZSI6IkFRRHRIbWwtakhjY25sQmxidDJmcGpDZmtLV2stb2FQY0lLbHpWQWtfMUlhLTNqMF9wdlhsaFUyTnJvYXRsT2lvUmJfSXNzc19oSXFyYzFRX3BLZ1RaX1RSTEhCbGpzRTFHZkFjWWJoX0Q4aVVwYWdSR2Q0bVNXcUVwai1SajlkT1J5RmxadzZHbWZCc0ZCbVdUY0RDNDAzUFVnTzV2TVBONk1UcmpSUDlpTU85dFdSc0hURFdsUVhrNDJycVhvbzM2SHlnYXRNdDJMRWlNNUZrcmVfRWtiWGUzTTlqdzY4enpKT2RVUjlIUmt2TUlXcWZqQ2RUc3FmYUo5MWowUF95bm9aLVZCSnpmb0xuSkt3MV9JTkFTQzdEZmM3ZURIeDFiTkFyRS1SQ1FhYUp3ZWtydVdzMFBYaV9pTDdYTlZrRTg5Yy1oYWVrWVI1YU45cDhwVXp0ZXBsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUhiWkNnM3M0UXJRZmhyOXRaQm5mdHI2cTlsYXJNMnpRaFpDZTNlczJOTGkwNGc4NGJaQldRTWs4VlpDWkNZMVZ3ak52azJ4M0d0VkxaQTdPajhZWkFkNklDdUxtMjI0NllhVTZQdXRlMk1PU3haQnpxbDhxUnU2UDhRYTZnRXhpUGRRbHB5WWJYSmVRczB3N2UzdFRxZXdnQWdUYXNpYzRjd0d3MHpaQUxTdXNCVUN3Y0JnVnk3MmdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2MjA3NDQ4fQ; rur="ODN\05455002803434\0541717743459:01f7dc2b656c6f698ae45a64240745cb3e01e62cb90350349fcf91dba76a5d92e481be60"',
    'Referer': 'https://www.instagram.com/5u2.a/',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Viewport-Width': '624',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': '1gI1BSItuCt7GpIB7BL3KCrapTfKligx',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR2f295htsHXPFyt6RxGipeoIQHM6Vikj5SuhBSAT7RgrCSq',
    'X-Requested-With': 'XMLHttpRequest',}
		rr = get(url,headers=headers).json()
		url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
		haha={
 'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
 'X-Pigeon-Rawclienttime':'1707104597.347',
 'X-IG-Connection-Speed':'-1kbps',
 'X-IG-Bandwidth-Speed-KBPS':'-1.000',
 'X-IG-Bandwidth-TotalBytes-B':'0',
 'X-IG-Bandwidth-TotalTime-MS':'0',
 'X-IG-VP9-Capable':'false',
 'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
 'X-IG-Connection-Type':'WIFI',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-App-ID':'567067343352427',
 'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
 'Accept-Language':'ar-IQ, en-US',
 'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Accept-Encoding':'gzip, deflate',
 'Host':'i.instagram.com',
 'X-FB-HTTP-Engine':'Liger',
 'Connection':'keep-alive',
 'Content-Length':'364',
 }
		ada={
 'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{user}''"}',
 
 'ig_sig_key_version':'4',
 }
		s=post(url,headers=haha,data=ada).text
		url = 'http://www.bradychrist.top/api/v7/user'
		he = {
'Host': 'www.bradychrist.top',
'Connection': 'keep-alive',
'Content-Length': '13',
'package': 'ins.bradychrist.com',
'apptype': 'android',
'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.211 Mobile Safari/537.36',
 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'idfa': '93f87de7-a83b-4098-a8a7-6801539c5f6a',
  'Accept': 'application/json, text/plain, */*',
  'pk': '',
  'username': '',
  'version': '1.0',
  'Origin': 'http://www.bradychrist.top',
  'X-Requested-With': 'ins.bradychrist.com',
  'Referer': 'http://www.bradychrist.top/h5_v12/',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
} 
		da=(f'username=ks_.j')
		zaid=post(url,headers=he,data=da).json()
		avatar=zaid['data']['avatar']
		id1=zaid['data']['userPk']
		pos=zaid['data']['postsNum']
		name = rr['data']['user']['full_name']
		bio = rr['data']['user']['biography']
		fol = rr['data']['user']['edge_followed_by']['count']
		fols = rr['data']['user']['edge_follow']['count']
		id = rr['data']['user']['id']
		if '"تم إرسال البريد الإلكتروني"' in s:
			try:
				rest = s.split('"email":"')[1].split('","status":"')[0]
			except:
				rest = 'Error'
		return {'name': name, 'user': user, 'email': f'{user}@gmail.com', 'follower': fol, 'folloers': fols,'posts': pos,'id': id, 'bio': bio,'image': avatar,'rest': rest, 'dev': 'https://t.me/d_xiim'}
	except:
		return {'error?': f'error/get/info/user?={user}', 'dev': 'https://t.me/d_xiim'}

app = Flask(__name__)
@app.route('/<num>/user=<text>')

def de(text,num):
	try:
		return {'done check': dd(text,int(num))}
	except:
		return {'bad': 'user not fond'}
