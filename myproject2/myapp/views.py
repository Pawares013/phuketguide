from django.shortcuts import render

# Create your views here.
# myapp/views.py
def my_view(request):
    context = {
        'image_url': 'static/448780348_2612913918915919_3968755390211366472_n',  # เปลี่ยนเป็นชื่อไฟล์รูปภาพของคุณ
        'facebook_link': 'https://www.facebook.com/profile.php?id=100017787245249',  # เปลี่ยนเป็นลิงก์ Facebook ของคุณ
        'name': 'นาย ปวเรศ ฮ่อบุตร',
        'student_id': '6649010013',
    }
    return render(request, 'myapp/my_template.html', context)
    return render(request, 'myapp/page.html', context)
    