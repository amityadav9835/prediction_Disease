from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignUpForm, build_prediction_form
from .ml import predict


DIABETES_FIELDS = [
    {"label": "Pregnancies", "placeholder": "generally between 0-17 according to the dataset"},
    {"label": "Glucose", "placeholder": "generally between 0-199 according to the dataset"},
    {"label": "BloodPressure", "placeholder": "generally between 0-122 according to the dataset"},
    {"label": "SkinThickness", "placeholder": "generally between 0-99 according to the dataset"},
    {"label": "Insulin", "placeholder": "generally between 0-846 according to the dataset"},
    {"label": "BMI", "placeholder": "generally between 0-67 according to the dataset"},
    {"label": "DiabetesPedigreeFunction", "placeholder": "generally between 0.078-2.420 according to the dataset"},
    {"label": "Age", "placeholder": "age"},
]

HEART_FIELDS = [
    {"label": "age", "placeholder": "age"},
    {"label": "sex", "placeholder": "enter 0 for female, 1 for male, according to the dataset"},
    {"label": "cp", "placeholder": "enter either 0, 1, 2, or 3 according to the dataset"},
    {"label": "trestbps", "placeholder": "generally between 94-200 according to the dataset"},
    {"label": "chol", "placeholder": "generally between 126-564 according to the dataset"},
    {"label": "fbs", "placeholder": "enter either 0 or 1 according to the dataset"},
    {"label": "restecg", "placeholder": "enter either 0, 1, or 2 according to the dataset"},
    {"label": "thalach", "placeholder": "generally between 71-202 according to the dataset"},
    {"label": "exang", "placeholder": "enter either 0 or 1 according to the dataset"},
    {"label": "oldpeak", "placeholder": "generally between 0-6.20 according to the dataset"},
    {"label": "slope", "placeholder": "enter either 0, 1, or 2 according to the dataset"},
    {"label": "ca", "placeholder": "enter either 0, 1, 2, 3, or 4 according to the dataset"},
    {"label": "thal", "placeholder": "enter either 0, 1, 2, or 3 according to the dataset"},
]

PARKINSONS_FIELDS = [
    {"label": "MDVP:Fo(Hz)", "placeholder": "generally between 88.333-260.105 according to the dataset"},
    {"label": "MDVP:Fhi(Hz)", "placeholder": "generally between 102.145-592.030 according to the dataset"},
    {"label": "MDVP:Flo(Hz)", "placeholder": "generally between 65.476-239.170 according to the dataset"},
    {"label": "MDVP:Jitter(%)", "placeholder": "generally between 0.001680-0.033160 according to the dataset"},
    {"label": "MDVP:Jitter(Abs)", "placeholder": "generally between 0.000007-0.000260 according to the dataset"},
    {"label": "MDVP:RAP", "placeholder": "generally between 0.000680-0.021440 according to the dataset"},
    {"label": "MDVP:PPQ", "placeholder": "generally between 0.000920-0.019580 according to the dataset"},
    {"label": "Jitter:DDP", "placeholder": "generally between 0.002040-0.064330 according to the dataset"},
    {"label": "MDVP:Shimmer", "placeholder": "generally between 0.009540-0.119080 according to the dataset"},
    {"label": "MDVP:Shimmer(dB)", "placeholder": "generally between 0.085000-1.302000 according to the dataset"},
    {"label": "Shimmer:APQ3", "placeholder": "generally between 0.004550-0.056470 according to the dataset"},
    {"label": "Shimmer:APQ5", "placeholder": "generally between 0.005700-0.079400 according to the dataset"},
    {"label": "MDVP:APQ", "placeholder": "generally between 0.007190-0.137780 according to the dataset"},
    {"label": "Shimmer:DDA", "placeholder": "generally between 0.013640-0.169420 according to the dataset"},
    {"label": "NHR", "placeholder": "generally between 0.000650-0.314820 according to the dataset"},
    {"label": "HNR", "placeholder": "generally between 8.441000-33.047000 according to the dataset"},
    {"label": "RPDE", "placeholder": "generally between 0.256570-0.685151 according to the dataset"},
    {"label": "DFA", "placeholder": "generally between 0.574282-0.825288 according to the dataset"},
    {"label": "spread1", "placeholder": "generally between -7.964984 to -2.434031 according to the dataset"},
    {"label": "spread2", "placeholder": "generally between 0.006274-0.450493 according to the dataset"},
    {"label": "D2", "placeholder": "generally between 1.423287-3.671155 according to the dataset"},
    {"label": "PPE", "placeholder": "generally between 0.044539-0.527367 according to the dataset"},
]


PREDICTORS = {
    "diabetes": {
        "title": "Diabetes Prediction",
        "fields": DIABETES_FIELDS,
        "positive": "This person has Diabetes",
        "negative": "This person doesn't have Diabetes",
    },
    "heart": {
        "title": "Heart Disease Prediction",
        "fields": HEART_FIELDS,
        "positive": "This person has Heart Disease",
        "negative": "This person doesn't have Heart Disease",
    },
    "parkinsons": {
        "title": "Parkinsons Prediction",
        "fields": PARKINSONS_FIELDS,
        "positive": "This person has Parkinson's",
        "negative": "This person doesn't have Parkinson's",
    },
}


def home(request):
    return render(request, "predictor/home.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def prediction_view(request, model_name):
    config = PREDICTORS[model_name]
    form_class = build_prediction_form(config["fields"])
    output_text = None

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            values = [form.cleaned_data[f"field{index}"] for index in range(1, len(config["fields"]) + 1)]
            result = predict(model_name, values)
            display_text = config["positive"] if result == 1 else config["negative"]
            output_text = f"Result: {display_text}"
    else:
        form = form_class()

    return render(
        request,
        "predictor/prediction_form.html",
        {
            "title": config["title"],
            "form": form,
            "output_text": output_text,
        },
    )


def diabetes(request):
    return prediction_view(request, "diabetes")


def parkinsons(request):
    return prediction_view(request, "parkinsons")


def heartdisease(request):
    return prediction_view(request, "heart")

# Create your views here.
