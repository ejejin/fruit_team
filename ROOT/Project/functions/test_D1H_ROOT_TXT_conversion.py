#from D1H_ROOT_TXT_conversion import D1H_txt_to_root, D1H_root_to_txt
from D1H_rootHist_TXT_conversion import D1H_txt_to_roothist, D1H_roothist_to_txt

#ROOT = D1H_txt_to_roothist("./_processed.txt","")
#TXT= D1H_roothist_to_txt("../junho/py-fillrandom.root",".")

#TXT = D1H_roothist_to_txt("Height1.root","/../");
TXT = D1H_roothist_to_txt("../junho/Height1.root",""); print(type(TXT)); print(TXT);
ROOT = D1H_txt_to_roothist("Height1_F.txt","../"); print(type(ROOT)); print(ROOT);



