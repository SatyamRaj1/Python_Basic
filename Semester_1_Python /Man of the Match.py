runs={'rb':50,'ns':90,'sg':70,'vk':90}
balls={'rb':70,'ns':90,'sg':87,'vk':10}
max=0
st=0
for i in runs:
       if runs[i]>max:
           max=runs[i]
           player=i
           st=runs[i]/balls[i]
       elif runs[i]==max:
           if runs[i]/balls[i]>st:
               player=i
print(player)       
       
