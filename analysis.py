#import glob
import pandas as pd
import os

#files = glob.glob('.\sourcecode')
directory= os.scandir('sourcecode')
captchasfound =0
recaptchasfound=0
captchasnotfound=0
whereCAPTCHAnotfound= ''
whereCAPTCHAfound= ''
captchaResult= ''
whereReCAPTCHAS= ''
recaptchaResult= ''
Totalinstances=0
hcaptchaResult= ''
hcaptchasfound= 0
whereHCAPTCHAS= ''

whereFUNCAPTCHAS= ''
FUNcaptchaResult = ''
FUNcaptchasfound = 0

FANCYcaptchaResult = ''
FANCYcaptchasfound = 0
whereFANCYCAPTCHAS= ''

jetpackResult= ''
jetpacksfound= 0
whereJETPACKS= ''

pxcaptchaResult= ''
pxcaptchasfound= 0
wherePXCAPTCHAS= ''

Notcharacterized = ''
notchars =0
urlsnotchar = ''


for fi in directory:
    with open(fi, encoding="utf-8") as f:
        fi =(str(fi))[10:]
        fi+= '\n'
        Totalinstances += 1
        content = f.read() 
        content= str(content)
        characterized=0
        found=0
        jetpackfound=0
        pxfound=0
        try:
                if (content.find('jetpack_protect') != -1) :# finds instance of captcha- all lowercase
                    x = content.find('jetpack_protect') +7
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1')
                    content= content[captchaStart:]
                    jetpackResult += "\n" + content
                    jetpacksfound += 1
                    jetpackfound=1
                    found =1

                if (content.find('recaptcha')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('recaptcha')+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    recaptchaResult+= "\n" + content[captchaStart:]
                    recaptchasfound += 1
                    whereReCAPTCHAS+= fi
                elif (content.find("RECAPTCHA")!= -1) : # finds instance of recaptcha-all upper
                    x = content.find("RECAPTCHA")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    recaptchaResult+= "\n" + content[captchaStart:]
                    recaptchasfound += 1
                    whereReCAPTCHAS+= fi
                elif (content.find("ReCaptcha")!= -1) :
                    x = content.find("ReCaptcha")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    recaptchaResult+= "\n" + content[captchaStart:]
                    recaptchasfound += 1
                    whereReCAPTCHAS+= fi
                elif (content.find("Recaptcha")!= -1) :
                    x = content.find("Recaptcha")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    recaptchaResult+= "\n" + content[captchaStart:]
                    recaptchasfound += 1
                    whereReCAPTCHAS+= fi
                elif (content.find("reCaptcha")!= -1) :
                    x = content.find("reCaptcha")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    recaptchaResult+= "\n" + content[captchaStart:]
                    recaptchasfound += 1
                    whereReCAPTCHAS+= fi


                if (content.find('hcaptcha')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('hcaptcha')+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    hcaptchaResult+= "\n" + content[captchaStart:]
                    hcaptchasfound += 1
                    whereHCAPTCHAS+= fi
                elif (content.find("HCAPTCHA")!= -1) : # finds instance of recaptcha-all upper
                    x = content.find("HCAPTCHA")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    hcaptchaResult+= "\n" + content[captchaStart:]
                    hcaptchasfound += 1
                    whereHCAPTCHAS+= fi
                elif (content.find("HCaptcha")!= -1) :
                    x = content.find("HCaptcha")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    hcaptchaResult+= "\n" + content[captchaStart:]
                    hcaptchasfound += 1
                    whereHCAPTCHAS+= fi
                elif (content.find("Hcaptcha")!= -1) :
                    x = content.find("Hcaptcha")+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    hcaptchaResult+= "\n" + content[captchaStart:]
                    hcaptchasfound += 1
                    whereHCAPTCHAS+= fi
                whereCAPTCHAfound+= fi

                if (content.find('fun-captcha')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('fun-captcha')+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    FUNcaptchaResult += "\n" + content[captchaStart:]
                    FUNcaptchasfound += 1
                    whereFUNCAPTCHAS+= fi

                if (content.find('fancycaptcha')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('fancycaptcha')+9
                    content= content[:x]
                    characterized =1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    FANCYcaptchaResult+= "\n" + content[captchaStart:]
                    FANCYcaptchasfound += 1
                    whereFANCYCAPTCHAS+= fi

                if (content.find('perimeterx')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('perimeterx')+9
                    content= content[:x]
                    characterized =1
                    found = 1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1') 
                    pxcaptchaResult+= "\n" + content[captchaStart:]
                    pxcaptchasfound += 1
                    wherePXCAPTCHAS+= fi
                    pxfound=1


                if (content.find('captcha') != -1) :# finds instance of captcha- all lowercase
                    x = content.find('captcha') +7
                    content= content[:x]
                    found=1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1')
                    content= content[captchaStart:]
                    captchaResult += "\n" + content
                    captchasfound += 1
                elif (content.find('CAPTCHA')!= -1) :# finds instance of captcha-all upper
                    x = content.find('CAPTCHA') +7
                    content= content[:x]
                    found=1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1')
                    captchaResult+= "\n" + content[captchaStart:]
                    captchasfound += 1
                elif (content.find('Captcha')!= -1) :# finds instance of captcha
                    x = content.find("Captcha")+7
                    content= content[:x]
                    found=1
                    try: ## finds result CAPTCHA and text before instance UNTIL SPEC CHAR
                        captchaStart = []
                        if 'http' in content :
                            f= content.rfind("http", 0, x)
                            captchaStart.append(content.rfind("http", 0, x))
                        if '?' in content :
                            captchaStart.append(content.rfind("?", 0, x))
                        if ':' in content :
                            captchaStart.append(content.rfind(":", 0, x))
                        if '_' in content :
                            captchaStart.append(content.rfind("_", 0, x))
                        if '"*' in content :
                            captchaStart.append(content.rfind("'*", 0, x))
                        if '\*' in content:
                            captchaStart.append(content.rfind("\*", 0, x))
                        captchaStart= max(captchaStart) # takes highest value- least amount of chars
                    except:
                        captchaStart.append(content.rfind("/", 0, x))
                        print('error at point 1')
                    captchaResult+= "\n" + content[captchaStart:]
                    captchasfound += 1
                elif (jetpackfound==0 | pxfound==0):
                    captchasnotfound +=1
                    whereCAPTCHAnotfound += fi
                    continue

                if (characterized==0):
                    if (found==1):
                        Notcharacterized += fi
                        Notcharacterized += content
                        notchars += 1
                        urlsnotchar= urlsnotchar + fi + '\n'
                
        except:
            print("error")

captchasfound = captchasfound + jetpacksfound + pxcaptchasfound
with open("AnalysisResults", "w", encoding="utf-8") as h:
        h.write(str(Totalinstances))
        h.write(' Totalinstances \n')
        j= '{}{}{}'.format('Captchas not found in ', captchasnotfound, ' files \n\n')
        h.write(j)
        h.write(str(whereCAPTCHAnotfound))
        k= '{}{}{}'.format('\nCaptchas found : ', captchasfound, '\n\n')
        h.write(k)
        h.write(str(whereCAPTCHAfound))
        l= '{}{}{}'.format('\nReCaptchas found : ', recaptchasfound, '\n\n')
        h.write(l)
        h.write(str(whereReCAPTCHAS))

with open("Notcharacterized", "w", encoding="utf-8") as h:
        m= '{}{}{}{}'.format(notchars, ' Notcharacterized \n', Notcharacterized, '\n')
        h.write(m)

with open("Notcharacterizedurls", "w", encoding="utf-8") as h:
        m= '{}{}{}{}'.format(notchars, ' Notcharacterized \n', urlsnotchar, '\n')
        h.write(m)

#CAPTCHA source code
with open("CAPTCHAInstances", "w", encoding="utf-8") as p:
        p.write(str(Totalinstances))
        p.write(' Totalinstances \n')
        
        k= '{}{}{}{}'.format(captchasfound,' CAPTCHAInstance Percentage : ', captchasfound/Totalinstances, '\n')
        p.write(k)
        j= '{}{}{}{}'.format(recaptchasfound, ' RECAPTCHAInstances \n', recaptchasfound/captchasfound, '\n')
        p.write(j)
        j= '{}{}{}{}'.format(hcaptchasfound, ' HCAPTCHAInstances \n', hcaptchasfound/captchasfound, '\n')
        p.write(j)
        j= '{}{}{}{}'.format(FUNcaptchasfound, ' FUNCAPTCHAInstances \n', FUNcaptchasfound/captchasfound, '\n')
        p.write(j)
        j= '{}{}{}{}'.format(FANCYcaptchasfound, ' FANCYCAPTCHAInstances \n', FANCYcaptchasfound/captchasfound, '\n')
        p.write(j)
        j= '{}{}{}{}'.format(jetpacksfound, ' JETPACK_PROTECT Instances \n', jetpacksfound/captchasfound, '\n')
        p.write(j)
        j= '{}{}{}{}'.format(pxcaptchasfound, ' PXCAPTCHA Instances \n', pxcaptchasfound/captchasfound, '\n')
        p.write(j)
        # k= '{}{}{}{}'.format(hcaptchasfound,' HCAPTCHAInstances \n', hcaptchaResult, '\n\n')
        # p.write(k)
        # k= '{}{}{}{}'.format(funcaptchasfound,' FUNCAPTCHAInstances \n', funcaptchaResult, '\n\n')
        # p.write(k)
        # k= '{}{}{}{}'.format(captchasfound,' CAPTCHAInstances \n', captchaResult, '\n\n')
        # p.write(k)
        # j= '{}{}{}{}'.format(recaptchasfound, ' RECAPTCHAInstances \n', recaptchaResult, '\n\n')
        # p.write(j)
