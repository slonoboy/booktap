from pydoc import describe
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Library(models.Model):
    library_name = models.CharField(max_length=100, null = True, blank = True)
    town = models.CharField(max_length=50, null = True, blank = True)      
    address = models.CharField(max_length=50, null = True, blank = True)
    call_number = models.CharField(max_length=50, null = True, blank = True)
    

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    phone_number = models.CharField(max_length=30, unique=False)
    id_number = models.CharField(max_length=30, unique=False)
    library_id = models.ForeignKey(Library,on_delete=models.CASCADE)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_librarian = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def str(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
    

class Book(models.Model):
    book_name = models.CharField(max_length=50,null = True, blank=False)
    author = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField(max_length=500, null = True, blank  = True)
    genres = models.CharField(max_length=150, blank = True)
    image = models.CharField(max_length=500)
    

class BookOwned(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    original_library = models.ForeignKey(Library, on_delete=models.CASCADE)
    #current_library = models.ForeignKey(Library, on_delete=models.CASCADE)
        
    
class Borrow(models.Model):
    borrow_date = models.DateField('date created', auto_now_add=True)
    return_date = models.DateField('return date', blank=True, default=None, null=True)
    isActive = models.BooleanField(default = True)
    book_id = models.ForeignKey(BookOwned, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    
class Review(models.Model):
    text = models.TextField(max_length=5000, null=False, blank=False)
    rating = models.BooleanField(null = True, blank= False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class Request(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    book_id = models.ForeignKey(BookOwned, on_delete=models.CASCADE)
    from_lib = models.ForeignKey(Library, on_delete=models.CASCADE)
    #to_lib = models.ForeignKey(Library, on_delete=models.CASCADE)
    request_date = models.DateField("date created", auto_now_add=True)
    deliver_date = models.DateField('deliver date', blank=True, default=None, null=True)
    isDelivering = models.BooleanField(default=True)
    isCancelled = models.BooleanField(default=False)
    
    
class Transaction(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(blank = True, null = True)
       

class SocialRating(models.Model):
    total_borrows = models.IntegerField(default=0)
    late_returns = models.IntegerField(default=0)
    total_requests = models.IntegerField(default=0)
    cancelled_requests = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    compliants_received = models.IntegerField(default=0)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    final_rating = models.IntegerField(default=0)