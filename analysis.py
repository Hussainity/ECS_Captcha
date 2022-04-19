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

for fi in directory:
    with open(fi, encoding="utf-8") as f:
        fi =(str(fi))[10:]
        fi+= '\n'
        Totalinstances += 1
        content = f.read() 
        content= str(content)
        try:
                if (content.find('captcha') != -1) :# finds instance of captcha- all lowercase
                    x = content.find('captcha') +7
                    content= content[:x]
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
                else :
                    captchasnotfound +=1
                    whereCAPTCHAnotfound += fi
                    continue
                if (content.find('recaptcha')!= -1) :# finds instance of recaptcha- all lowercase
                    x = content.find('recaptcha')+9
                    content= content[:x]
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
                whereCAPTCHAfound+= fi
        except:
            print("error")
        
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

#CAPTCHA source code
with open("CAPTCHAInstances", "w", encoding="utf-8") as p:
        p.write(str(Totalinstances))
        p.write(' Totalinstances \n')
        k= '{}{}{}{}'.format(captchasfound,' CAPTCHAInstances \n', captchaResult, '\n\n')
        p.write(k)
        j= '{}{}{}{}'.format(recaptchasfound, ' RECAPTCHAInstances \n', recaptchaResult, '\n\n')
        p.write(j)
