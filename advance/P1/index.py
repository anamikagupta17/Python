#import 1
import Admin.product
import Admin.Common.header
import Tech.profile
from Admin.Common.header import header
import user.request
Admin.product.admin_product()
Admin.Common.header.header()
Tech.profile.tech_profile()
user.request.user_request()
print()

#import 2
from Admin import service
from Admin.Common import footer
service.admin_service() 
footer.footer()
print()

#import 3
from user.profile import user_profile  #package.module from import function
from Tech.profile import tech_profile
user_profile()
tech_profile()
print()

#import 4
from Admin.Common import *
from Admin import *
header.header()
service.admin_service()

