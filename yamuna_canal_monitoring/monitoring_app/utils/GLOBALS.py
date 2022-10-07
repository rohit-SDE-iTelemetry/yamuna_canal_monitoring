from django.contrib.auth.models import Permission

# permission object for views
permissionObj = Permission.objects.all()

# filter permissions for current loged in user
def get_permissions(request):
    permissions = Permission.objects.filter(user=request.user)
    return permissions

# excluded permissions for add users
exlude_permissions = ['Can add log entry',
                      'Can change log entry',
                      'Can delete log entry',
                      'Can view log entry',
                      'Can add group',
                      'Can change group',
                      'Can delete group',
                      'Can view group',
                      'Can add permission',
                      'Can change permission',
                      'Can delete permission',
                      'Can view permission',
                      'Can add content type',
                      'Can change content type',
                      'Can delete content type',
                      'Can view content type',
                      'Can add session',
                      'Can change session',
                      'Can delete session',
                      'Can view session'
                    ]