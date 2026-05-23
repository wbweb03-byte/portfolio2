import uuid
from django.db import models


class Students(models.Model):

    student_id = models.CharField(
        max_length=8,
        unique=True,
        editable=False
    )

    name = models.CharField(max_length=100)

    picture = models.ImageField(
        upload_to="students/"
    )

    dob = models.DateField()

    father_name = models.CharField(
        max_length=100
    )

    contact = models.CharField(
        max_length=12,
        unique=True
    )

    class_roll = models.CharField(
        max_length=100
    )

    village = models.CharField(
        max_length=100
    )

    p_o = models.CharField(
        max_length=100
    )

    p_s = models.CharField(
        max_length=100
    )

    dist = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pin = models.CharField(
        max_length=10
    )

    create_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-create_at']

    def save(self, *args, **kwargs):

        if not self.student_id:

            self.student_id = str(
                uuid.uuid4()
            )[:8].upper()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name