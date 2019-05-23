import requests;from bs4 import BeautifulSoup
def AdityaMangakyo(t:int=None):
	if t == None:url ='http://mangakyo.net/'
	else:
		url ='http://mangakyo.net/page/{}/'.format(int(t))
	r=requests.get(url)
	ss = BeautifulSoup(r.text,'html5lib')
	s = ss.select('div.lch > div.ch > div.l > h3 > a.series')
	sa = ss.select('div.lch > div.ch > div.l > ul > li > a')
	h = 'Mangakyo List'
	if s == []:
		return 'Manga Series Tidak Di Temukan'
	try:no= (int(t)-1)*15;zzz=(int(t)-1)*15+1
	except:no=0;zzz=1
	for a in range(len(s)):
		no+=1
		if no == zzz:
			zz = ''
			ass = 0
			hgg = [i.text for i in sa[a*3 : (a+1)*3]]
			hgg.sort()
			for i in hgg:
				ass+=1
				if ass % 3 == 0:zz+= '\n               {}'.format(i)
				else:
					if ass == 1:zz+= ' {}'.format(i)
					else:zz+= ',  {}'.format(i)
			h+= '\n {}. {}\n     {}'.format(no,s[a].text,zz)
		else:
			zz = ''
			ass = 0
			hgg = [i.text for i in sa[a*3 : (a+1)*3]]
			hgg.sort()
			for i in hgg:
				ass+=1
				if ass % 3 == 0:zz+= '\n               {}'.format(i)
				else:
					if ass == 1:zz+= ' {}'.format(i)
					else:zz+= ',  {}'.format(i)
			h+= '\n\n {}. {}\n     {}'.format(no,s[a].text,zz)
	return h