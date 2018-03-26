from socket import *
import base64

msg = "\r\n Computer Networks!!!!!!!!"
endmsg = "\r\n.\r\n"
sender = "<patrickwatters1995@gmail.com>"
recipient = "<patrickwatters1995@gmail.com>"
username = "patrickwatters1995@gmail.com"
password = ''

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket()
clientSocket.connect(("smtp.gmail.com", 587))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# ---------------------------------------------------------------------------

# Need encrypted connection
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand)
tls_recv = clientSocket.recv(1024)
print tls_recv
if tls_recv[:3] != '220':
	print '220 reply not received from server'

ssl_clientSocket = socket.ssl(clientSocket)

# Send the AUTH LOGIN command 
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand)
auth_recv = ssl_clientSocket.read(1024)
print auth_recv
if auth_recv[:3] != '334':
	print '334 reply not received from server'

# Send username
usnm = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(usnm)
usnm_recv = ssl_clientSocket.read(1024)
print usnm_recv
if uname_recv[:3] != '334':
	print '334 reply not received from server'

# Send password
pswd = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pswd)
pword_recv = ssl_clientSocket.read(1024)
print pword_recv
if pword_recv[:3] != '235':
	print '235 reply not received from server'

# Send MAILFROM command 
mailFromCommand = 'MAIL FROM: <patrickwatters1995@gmail.com>\r\n'
ssl_clientSocket.write(mailFromCommand)
recv2 = ssl_clientSocket.read(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

# Send RCPTTO command
rcptToCommand = 'RCPT TO: <patrickwatters1995@gmail.com>\r\n'
ssl_clientSocket.write(rcptToCommand)
recv3 = ssl_clientSocket.read(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'

# Send DATA command
dataCommand = 'DATA\r\n'
ssl_clientSocket.write(dataCommand)
recv4 = ssl_clientSocket.read(1024)
print recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'

ssl_clientSocket.write(msg)
ssl_clientSocket.write(endmsg)
recv5 = ssl_clientSocket.read(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'

# Send QUIT command
quitCommand = 'QUIT\r\n'
ssl_clientSocket.write(quitCommand)
recv6 = ssl_clientSocket.read(1024)
print recv6
if recv6[:3] != '221':
	print '221 reply not received from server.'

clientSocket.close()