from pygame import *
from random import *

black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
blue=(0,255,255)

init()
window= display.set_mode((500,530))
clock=time.Clock()
Font=font.SysFont("comicsansms",22)


N=100
tabx=[]
taby=[]
for i in range(N):
	tabx.append(randint(0,500))
	taby.append(randint(0,500))
	


end=False
while not end:
	for z in event.get():
		if z.type ==QUIT:
			end=True
	keys=key.get_pressed()
	if keys[K_a]:
		N=N+100
	for i in range(100):
		tabx.append(randint(0,500))
		taby.append(randint(0,500))	
	
	in_circle=0.0	
	window.fill(black)
	
	for i in range(N):
		
		if (tabx[i]-250)**2+(taby[i]-250)**2<=250**2:
			in_circle=in_circle+1
			window.set_at((tabx[i],taby[i]),blue)
		else:
			window.set_at((tabx[i],taby[i]),white)
		
	p=in_circle/N*500*500
	Pi=p/500/500*4
	
	text=Font.render("N="+str(N)+" p="+str(p)+" Pi="+str(Pi),True,yellow)
	window.blit(text,(20,503))
	
	clock.tick(10)
	display.flip()