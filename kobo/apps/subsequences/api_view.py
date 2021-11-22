from rest_framework.decorators import api_view
from rest_framework.response import Response

from kobo.apps.subsequences.models import SubmissionExtras

from kpi.models import Asset


@api_view(['POST', 'PATCH', 'GET'])
def advanced_submission_post(request):
    posted_data = request.data
    submission_uuid = request.data['submission_uuid']
    asset_uid = request.data['asset_uid']
    asset = Asset.objects.get(uid=asset_uid)
    try:
        submission = asset.submissions.get(uuid=submission_uuid)
    except SubmissionExtras.DoesNotExist:
        submission = asset.submissions.create(uuid=submission_uuid)
    submission.patch_content(request.data)
    # what does the front end want back?
    return Response(submission.content)
