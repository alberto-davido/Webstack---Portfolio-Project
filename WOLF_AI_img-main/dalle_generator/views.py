from django.shortcuts import render
import openai


def generate_image(request):
    api_key = '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'
    prompt = request.GET.get('prompt', 'Generate an image')
    size = request.GET.get('size', '256x256')
    num_images = 3

    openai.api_key = api_key

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=size
        )

        images = []
        for image_data in response['data']:
            image_url = image_data['url']
            images.append(image_url)

        return render(request, 'dalle_generator/generate_image.html', {'images': images})

    except Exception as e:
        error_message = str(e)
        return render(request, 'dalle_generator/error.html', {'error_message': error_message})
 
def profile(request):
    return render(request, 'profile.html')