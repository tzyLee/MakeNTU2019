from flask import Flask, send_file, request, jsonify
from src.text_to_speech import speak
from json import loads

app = Flask(__name__,
            template_folder='public', static_folder='public', static_url_path='')

test_paragraphs = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras et dui id tortor dignissim sagittis. Aliquam tristique sapien et vehicula placerat. Proin quis tellus eget elit mollis pretium id vitae nibh. Vestibulum rhoncus justo nibh, eu ornare turpis porttitor ac. Duis semper dolor a massa venenatis, vitae varius eros vestibulum. Morbi accumsan scelerisque nulla ac gravida. Fusce quis venenatis odio, eu tempus odio. Morbi facilisis dictum egestas. Nulla quis fringilla tellus, quis ullamcorper sem. Proin ullamcorper nisi nunc, id sagittis eros feugiat a. Donec mollis neque mollis leo consequat, eget tincidunt enim dignissim. Donec imperdiet erat nec congue malesuada. Suspendisse tristique ante sed lacus malesuada, a scelerisque urna viverra. Sed lacinia ligula ultricies purus fringilla varius. Quisque erat lorem, laoreet a risus a, volutpat porttitor tellus. Proin bibendum eu lectus id venenatis.',
    'Mauris feugiat facilisis augue accumsan pulvinar. In interdum vulputate odio. Sed ultrices vitae turpis nec porta. Sed luctus condimentum bibendum. Nam tempor consequat nulla, quis luctus dui lobortis eget. Curabitur porttitor, ipsum ut consectetur rhoncus, mi enim finibus neque, ut semper risus ante eu sapien. Aenean lacinia pellentesque nulla eget elementum. Cras finibus ullamcorper molestie. Donec ex magna, luctus nec ex et, convallis tincidunt est. Donec scelerisque risus arcu, at egestas lorem hendrerit a. Curabitur non enim gravida, dignissim magna at, ultrices orci. Etiam hendrerit, mi sit amet dapibus vulputate, lorem nulla dictum tortor, id varius massa urna at erat. Nullam felis nisl, maximus sed facilisis quis, ornare at mauris.',
    'In vitae ipsum commodo, congue elit vitae, accumsan orci. Vestibulum consectetur magna a arcu auctor vehicula. Fusce at lacus eget velit pellentesque facilisis eget egestas risus. Vivamus placerat et quam sed faucibus. Pellentesque augue arcu, imperdiet mattis eleifend ac, tincidunt ut neque. Suspendisse eu magna mattis lacus fringilla eleifend in vel leo. Ut ultricies tortor quis sollicitudin auctor. Praesent eu ante vitae dui luctus pulvinar in et lorem. Aenean fermentum fermentum mollis. Nam ac odio suscipit, congue diam at, pellentesque tortor. Phasellus sodales commodo enim vel interdum.',
    'In auctor lacinia pellentesque. Vivamus pharetra sapien ut elit pulvinar, vel finibus nulla vestibulum. Fusce sapien leo, imperdiet ut mauris ut, consequat condimentum arcu. Fusce ullamcorper condimentum est. Nullam turpis enim, scelerisque at pellentesque vitae, congue at enim. Praesent nec sem eleifend, ornare tortor eu, aliquam lacus. Nullam blandit consequat est sed tempor. Sed volutpat eu purus ut gravida. Phasellus egestas efficitur finibus. Etiam posuere elementum sapien, congue dapibus ex. Integer eu auctor felis. Nullam ac facilisis mauris. Vivamus efficitur ex ut fringilla placerat. Phasellus sed congue eros, sed dapibus turpis. Nullam ligula enim, feugiat tempus augue sollicitudin, vestibulum cursus magna. Sed in dolor condimentum, volutpat purus at, suscipit nulla.',
    'Aliquam nulla lorem, finibus ut facilisis vitae, mattis in ante. Etiam rutrum velit sed mi pulvinar placerat. Aliquam aliquet luctus elit, sed pulvinar libero hendrerit quis. Mauris bibendum tempus congue. Mauris porttitor purus ut condimentum varius. Duis ut erat condimentum, luctus nibh eget, lobortis nulla. Curabitur lorem ante, mattis nec facilisis eu, euismod sit amet velit. Nunc scelerisque aliquam tincidunt. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec sodales, libero quis viverra porta, eros velit scelerisque diam, vehicula sollicitudin leo arcu eu odio. Vivamus posuere luctus neque. Morbi ac nisl nec diam sodales condimentum a sed nisi. In id tincidunt dolor.'
]


@app.route("/")
def index():
    return send_file('public/index.html')


counter = 0


@app.route("/page", methods=['POST'])
def get_page():
    global counter
    counter += 1
    counter %= 5
    # data = loads(request.data)
    # speak(str(data['test']))
    return jsonify({'page': test_paragraphs[counter]})


if __name__ == "__main__":
    app.run()