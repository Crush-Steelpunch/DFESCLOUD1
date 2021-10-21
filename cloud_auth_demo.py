import cloud_auth

devcloud = cloud_auth.cloud_login()
devcloud.username = 'leon'
devcloud.password = 'password123'
devcloud.url = 'https://dev.company.com/login'


devcloud.login()

devcloud.create_vm('name',2,256)


productioncloud = cloud_auth.cloud_login()
productioncloud.username = 'leon'
productioncloud.password = 'password123'
productioncloud.url = 'https://cloud.company.com/login'

productioncloud.login()

productioncloud.create_vm('name12',2,1024)

for i in range(5):
    productioncloud.list_vm()
    devcloud.list_vm()

