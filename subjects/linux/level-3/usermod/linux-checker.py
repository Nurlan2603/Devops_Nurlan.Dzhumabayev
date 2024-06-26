def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_user(s):
    login = "marktwain"
    expected = "marktwain"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_password(s):
    login = "marktwain"
    password = "marktwain1835"
    passhash_script = "mkpasswd -m sha-512 \'{}\' $(sudo cat /etc/shadow | grep {} | cut -d ':' -f2 - | cut -d '$' -f3 -)".format(password, login)
    hashedpass_script = "sudo cat /etc/shadow | grep {} | cut -d ':' -f2 -".format(login)
    passhash_cmd = s.run(passhash_script)
    hashedpass_cmd = s.run(hashedpass_script)
    assert passhash_cmd == hashedpass_cmd, "incorrect password"
