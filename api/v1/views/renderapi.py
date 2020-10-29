
import os
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from s3_interaction import list_files, download_file, upload_file
from resume_render.render import create_resume

BUCKET = "hovify"

@app_views.route('/upload', methods=['POST'], strict_slashes=False)
def post_upload():
    if request.method == "POST":
        data = request.get_json()
        paths = create_resume(color="Red", data=data,
                              file_name=data.get("User").get("FirstName"))
        
        pdf = upload_file(paths[0], BUCKET) # saving pdf
        prev = upload_file(paths[1], BUCKET) # saving png preview

        os.system("find ./renders/ -type f -not -name 'altacv.cls' -exec rm {} \;")
        os.system("rm thumbnails/*.png")

        return jsonify({"pdf": pdf,"preview": prev})


# @app.route("/download/<filename>", methods=['GET'])
# def download(filename):
#     if request.method == 'GET':
#         output = download_file(filename, BUCKET)

#         return send_file(output, as_attachment=True)
