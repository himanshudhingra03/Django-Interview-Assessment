# from django.contrib.auth.base_user import BaseUserManager
# # from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import gettext_lazy as _




# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model where the email address is the unique identifier
#     and has an is_admin field to allow access to the admin app 
#     """
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_("The email must be set"))
#         if not password:
#             raise ValueError(_("The password must be set"))
#         email = self.normalize_email(email)

#         employee = self.model(email=email, **extra_fields)
#         employee.set_password(password)
#         employee.save()
#         return employee

# def create_superuser(self, username, password, email, created_at):
#         employee= self.create_user(email, password)
#         employee.is_admin = True
#         employee.save(using=self._db)
#         return employee