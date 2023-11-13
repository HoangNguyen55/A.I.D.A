from django.contrib import admin
from .models import PendingUser, ApprovedUser
from .forms import PendingUserForm
from django.contrib.auth import get_user_model
import uuid

@admin.register(PendingUser)
class PendingUserAdmin(admin.ModelAdmin):
    form = PendingUserForm
    actions = ['approve_user']  # to approve a pending user
    list_display = ('username', 'email')  # show the following columns on admin page

    @admin.action(description='Approve')
    def approve_user(self, request, queryset):
        User = get_user_model()

        # Iterate through selected PendingUser objects
        for pending_user in queryset:
            # Create a new ApprovedUser object with the same data
            approved_user = ApprovedUser.objects.create(
                id = uuid.uuid4(),
                username=pending_user.username,
                password=pending_user.password,
                email=pending_user.email,
            )

            # Delete the PendingUser
            pending_user.delete()

        self.message_user(request, 'Selected users have been approved and moved to User model.')


admin.site.register(ApprovedUser)
