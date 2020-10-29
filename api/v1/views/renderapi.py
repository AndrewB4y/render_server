
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from s3_interaction import list_files, download_file, upload_file
from resume_render.render import create_resume

UPLOAD_FOLDER = "uploads"
BUCKET = "hovify"

@app_views.route('/upload', methods=['POST'], strict_slashes=False)
def post_upload():
    if request.method == "POST":
        data = request.get_json()
        paths = create_resume(color="Red", data=data,
                              file_name=data.get("User").get("FirstName"))
        
        upload_file(paths[0], BUCKET) # saving pdf
        upload_file(paths[1], BUCKET) # saving png preview

        return jsonify({"pdf": ,"preview": })


# @app.route("/download/<filename>", methods=['GET'])
# def download(filename):
#     if request.method == 'GET':
#         output = download_file(filename, BUCKET)

#         return send_file(output, as_attachment=True)
