# # # import pymongo
# # # import base64
# # # from pymongo import MongoClient

# # # cluster =MongoClient("mongodb+srv://himanshu7:hatekube000@cluster0-umtto.mongodb.net/test?retryWrites=true&w=majority")
# # # db = cluster["resume"]
# # # collection = db["coll_resume"]

# # # with open(r"C:\Users\HimanshuKholiya\Downloads\GITresume\GITresume\Resume\Vihas Enquero.pdf", "rb") as pdf_file:
# # #     encoded_string = base64.b64encode(pdf_file.read())

# # # abc=db.coll_resume.insert_one({"_id":0, "image":encoded_string})


# # <old working file>

# # <!-- <body style="background-image: url('/static/black pattern.jpg');"> -->

# #   <!DOCTYPE html>
# # <html lang="en">
# # <head>
# #   <meta charset="UTF-8">
# #   <title>Enquero resume upload portal</title>
# #   <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/main1.css') }}">
# #   <meta name="viewport" content="width=device-width, initial-scale=1">
# # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
# # </head>
# # <body style="background-image: url('/static/ee.jpg');margin-left: 470px;">
# #   <div style="background-image: url('/static/dd.jpg');border-radius: 10px; width: 500px; height: 620px; padding-top:42px;margin: 50px; border: .1px solid black;box-shadow: 10px 20px 20px 10px rgba(0, 0, 0, 0.2), 10px 20px 20px 0px rgba(0, 0, 0, 0.19), 10px 20px 20px 0px rgba(0, 0, 0, 0.19)">
# #     <img style="position: sticky; width: 200px;" src="{{ url_for('static', filename='logo.png') }}" alt="enquero.com">
# #     <h1 class="ff" style="padding-top:35px;color:white;">Resume Upload</h1> 
   
# #     <form action="/forward/" method="POST"> 
# #         <label for="file" style="margin-bottom:90px;margin-top:100px;" class="btn btn-default btn-file">
# #             <i class="fa fa-file-text" style="font-size:80px;color:red">
# #             <input type="file" name="picture" id="file" style="display: none;">
# #         </i>
# #         </label>

# #         <level for="file" id="selector"></level>

# #         <div class="wrap">
# #           <button class="button" style="vertical-align:middle"><span>Submit </span></button> 
# #           </div> 
# #     </form>
# #     <h3 style="font-family: Arial, Helvetica, sans-serif;color:rgba(206, 32, 32, 0.753);"> {{ forward_message }}</h3> 
# #  </div>
# #  <footer style="font-family: Arial, Helvetica, sans-serif;color:black;font-size:15px;padding-right:450px;margin-top:-28px">Created by LazyCoders &copy;</footer>



# #  <script>
# #   var loader = function(e)
# #   {
# #     let file = e.target.files;
# #     let show = <span>Selected file:</span> + file[0].name;
  
# #     let output =document.getElementById("selector");
# #     output.innerHTML = show;
# #     output.classList.add("active");
# #   };
  
# #   let fileInput = document.getElementById("file");
# #   fileInput.addEventListener("change", loader);
# #   </script>

# # </body>

# # </html> 


# <old connection to atlas file working>

# from flask import Flask, render_template, Response, request, redirect, url_for
# import pymongo
# import base64
# from pymongo import MongoClient
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/forward/", methods=['POST'])
# def move_forward():
#     cluster =MongoClient("mongodb+srv://himanshu7:hatekube000@cluster0-umtto.mongodb.net/test?retryWrites=true&w=majority")
#     db = cluster["resume"]
#     collection = db["coll_resume"]

#     with open(r"C:\Users\HimanshuKholiya\Downloads\GITresume\GITresume\Resume\tar23.pdf", "rb") as pdf_file:
#         encoded_string = base64.b64encode(pdf_file.read())

#     abc=db.coll_resume.insert_one({"image":encoded_string})
#     forward_message = "File Uploaded !"
#     return render_template('index.html', forward_message=forward_message);

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=7000, debug=True)