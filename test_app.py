def test_homepage(client):
    """ اختبار صفحة الرئيسية """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Portfolio" in response.data

def test_contact_get(client):
    """ اختبار فتح صفحة الاتصال """
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact Me" in response.data

def test_contact_post(client):
    """ اختبار إرسال البيانات من صفحة الاتصال """
    response = client.post('/contact', data={
        'name': 'Mohanad Ahmed',
        'email': 'mohanad@example.com',
        'message': 'This is a test message.'
    })

    # التحقق من نجاح إرسال الرسالة
    assert response.status_code == 302  # 302 = إعادة توجيه (Redirect)
    assert b'Your message has been sent successfully!' not in response.data  # تأكد أن رسالة النجاح ليست في الرد المباشر

def test_invalid_email(client):
    """ اختبار إرسال بريد إلكتروني غير صالح """
    response = client.post('/contact', data={
        'name': 'Mohanad Ahmed',
        'email': 'invalid-email',
        'message': 'This is a test message.'
    })
    assert response.status_code == 200
    assert b'Invalid email address' in response.data
