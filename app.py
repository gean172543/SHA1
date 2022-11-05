from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    sha = ''
    text= ''
    if request.method == "POST":
        text = request.form['strex']
        if text == "":
            return render_template("index.html")
        A,B,C,D,E = sha_1(text)
        sha = (A+B+C+D+E).upper()
    return render_template("index.html", sha=sha,text=text)

def binaryToHexadecimal(n):
    # convert binary to int
    num = int(n, 2)
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    return(hex_num)

def decimalToBinary(n):
    return "{0:b}".format(int(n))

def sha_1(text):
    text_binary = ''.join(format(ord(i), '08b') for i in text)
    tmp = ''
    len_text = len(text_binary)
    tmp_len_text_binary = decimalToBinary(len_text)
    tmp_len_text_binary = f"{int(tmp_len_text_binary):064d}"

    text_binary += "1"
    for i in range(len(text_binary) , 448):
        text_binary += "0"

    text_binary += tmp_len_text_binary

    W = []
    for t in range(80):
        if t == 0:
            W.append(binaryToHexadecimal(text_binary[0:32]))
        elif t >0 and t<16:
            W.append(binaryToHexadecimal(text_binary[32*t:32*(t+1)]))
        else :
            W.append(hex(int(W[t-16],16) ^ int(W[t-14],16) ^ int(W[t-8],16) ^ int(W[t-3],16))[2:])


    A = "67452301" 
    B = "EFCDAB89" 
    C = "98BADCFE" 
    D = "10325476" 
    E = "C3D2E1F0"

    K = ["5a927999","6ed9eba1","9f1bbcdc","ca62c1d6"]

    # K0
    for t in range(20):
        tmp1 = hex( (int(B,16) & int(C,16)) | (~int(B,16) & int(D,16)) )
        tmp1 = hex( (int(tmp1,16) + int(E,16)) % int("100000000",16) )
        A_shift_5 = f"{int(A,16):032b}"[5:] + f"{int(A,16):032b}"[0:5]
        A_shift_5 = binaryToHexadecimal(A_shift_5)
        tmp1 = hex( (int(tmp1,16) + int(A_shift_5,16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(W[t],16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(K[0],16)) % int("100000000",16) )
        B_shift_30 = f"{int(B,16):032b}"[30:] + f"{int(B,16):032b}"[0:30]
        B_shift_30 = binaryToHexadecimal(B_shift_30)
        E = D
        D = C
        B = A
        A = tmp1[2:]
        C = B_shift_30
        # if i==5:
        #     return A,B,C,D,E
        
    # K1
    for t in range(20,40):
        tmp1 = hex( int(B,16) ^ int(C,16) ^ int(D,16) ) 
        tmp1 = hex( (int(tmp1,16) + int(E,16)) % int("100000000",16) )
        A_shift_5 = f"{int(A,16):032b}"[5:] + f"{int(A,16):032b}"[0:5]
        A_shift_5 = binaryToHexadecimal(A_shift_5)
        tmp1 = hex( (int(tmp1,16) + int(A_shift_5,16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(W[t],16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(K[1],16)) % int("100000000",16) )
        B_shift_30 = f"{int(B,16):032b}"[30:] + f"{int(B,16):032b}"[0:30]
        B_shift_30 = binaryToHexadecimal(B_shift_30)
        E = D
        D = C
        B = A
        A = tmp1[2:]
        C = B_shift_30
        
    # K2
    for t in range(40,60):
        tmp1 = hex( (int(B,16) & int(C,16)) | (int(B,16) & int(D,16)) | (int(C,16) & int(D,16)) ) 
        tmp1 = hex( (int(tmp1,16) + int(E,16)) % int("100000000",16) )
        A_shift_5 = f"{int(A,16):032b}"[5:] + f"{int(A,16):032b}"[0:5]
        A_shift_5 = binaryToHexadecimal(A_shift_5)
        tmp1 = hex( (int(tmp1,16) + int(A_shift_5,16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(W[t],16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(K[2],16)) % int("100000000",16) )
        B_shift_30 = f"{int(B,16):032b}"[30:] + f"{int(B,16):032b}"[0:30]
        B_shift_30 = binaryToHexadecimal(B_shift_30)
        E = D
        D = C
        B = A
        A = tmp1[2:]
        C = B_shift_30
        
    # K3
    for t in range(60,80):
        tmp1 = hex( int(B,16) ^ int(C,16) ^ int(D,16) ) 
        tmp1 = hex( (int(tmp1,16) + int(E,16)) % int("100000000",16) )
        A_shift_5 = f"{int(A,16):032b}"[5:] + f"{int(A,16):032b}"[0:5]
        A_shift_5 = binaryToHexadecimal(A_shift_5)
        tmp1 = hex( (int(tmp1,16) + int(A_shift_5,16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(W[t],16)) % int("100000000",16) )
        tmp1 = hex( (int(tmp1,16) + int(K[3],16)) % int("100000000",16) )
        B_shift_30 = f"{int(B,16):032b}"[30:] + f"{int(B,16):032b}"[0:30]
        B_shift_30 = binaryToHexadecimal(B_shift_30)
        E = D
        D = C
        B = A
        A = tmp1[2:]
        C = B_shift_30
    return A,B,C,D,E

app.run(host="0.0.0.0", port=80, debug=True) 