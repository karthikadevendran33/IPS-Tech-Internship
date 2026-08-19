from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)


# =========================================================
# HTML
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="ta">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>திருக்குறள்</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;

            font-family:
                "Noto Sans Tamil",
                "Segoe UI",
                Arial,
                sans-serif;

            background:
                linear-gradient(
                    180deg,
                    #f8efd9,
                    #ead8ae
                );

            color: #4a2f19;
        }


        /* ================= HEADER ================= */

        .header {
            width: 100%;
            height: 72px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 25px 0 48px;

            background: #633b1f;

            box-shadow:
                0 3px 12px
                rgba(0, 0, 0, 0.22);

            position: relative;
            z-index: 100;
        }


        .logo {
            display: flex;
            align-items: center;

            gap: 12px;

            color: #f9e8bd;

            font-size: 27px;
            font-weight: 700;
        }


        .logo-icon {
            font-size: 35px;
        }


        /* ================= MENU ================= */

        .menu-button {
            width: 48px;
            height: 48px;

            border: none;
            background: transparent;

            cursor: pointer;

            display: flex;
            flex-direction: column;

            align-items: center;
            justify-content: center;

            gap: 6px;
        }


        .menu-button span {
            width: 38px;
            height: 4px;

            border-radius: 5px;

            background: #f8e6b9;

            display: block;
        }


        .menu-button:hover span {
            background: white;
        }


        /* ================= LANGUAGE MENU ================= */

        .side-menu {
            position: absolute;

            top: 65px;
            right: 18px;

            width: 170px;

            padding: 8px;

            background: #fff9e9;

            border: 1px solid #b68a4e;

            border-radius: 10px;

            box-shadow:
                0 8px 25px
                rgba(0, 0, 0, 0.25);

            display: none;
        }


        .side-menu.active {
            display: block;
        }


        .menu-title {
            padding: 10px 12px 8px;

            font-size: 13px;
            font-weight: 600;

            color: #8a633b;
        }


        .language-button {
            width: 100%;

            padding: 11px 12px;

            border: none;

            background: transparent;

            border-radius: 7px;

            text-align: left;

            font-size: 15px;

            color: #4b301a;

            cursor: pointer;
        }


        .language-button:hover {
            background: #ead5ad;
        }


        /* ================= MAIN ================= */

        .main {
            min-height:
                calc(100vh - 72px);

            display: flex;

            flex-direction: column;

            align-items: center;

            padding:
                65px 20px 80px;
        }


        .search-title {
            font-size: 28px;

            font-weight: 600;

            color: #633d20;

            margin-bottom: 15px;
        }


        /* ================= SEARCH ================= */

        .search-area {
            display: flex;

            align-items: center;

            gap: 12px;
        }


        .search-box {
            width: 345px;
            height: 68px;

            border:
                3px solid #b17b3e;

            border-radius: 38px;

            background: #fffaf0;

            padding: 0 28px;

            font-size: 21px;

            color: #4b2e18;

            outline: none;
        }


        .search-box:focus {
            border-color: #74451f;

            box-shadow:
                0 0 0 4px
                rgba(153, 108, 57, 0.12);
        }


        .search-button {
            width: 68px;
            height: 68px;

            border: none;

            border-radius: 50%;

            background: #75431f;

            color: white;

            font-size: 25px;

            cursor: pointer;

            box-shadow:
                0 5px 12px
                rgba(0, 0, 0, 0.20);
        }


        .search-button:hover {
            background: #552e16;
        }


        .range-text {
            margin-top: 12px;

            font-size: 16px;

            color: #8b6843;
        }


        .error {
            min-height: 25px;

            margin-top: 12px;

            color: #bd2727;

            font-size: 16px;

            text-align: center;
        }


        /* ================= RESULT ================= */

        #result {
            width: 100%;

            display: flex;

            flex-direction: column;

            align-items: center;

            margin-top: 28px;
        }


        .kural-number {
            font-size: 16px;

            font-weight: 600;

            color: #805b37;

            margin-bottom: 13px;
        }


        /* ================= PALM LEAF ================= */

        .palm-leaf {
            position: relative;

            width: min(850px, 94vw);

            padding: 30px 65px;

            margin-bottom: 24px;

            display: flex;

            align-items: center;

            justify-content: center;

            text-align: center;

            background:
                linear-gradient(
                    180deg,
                    #d5b16d 0%,
                    #ecd49a 48%,
                    #d4ad65 100%
                );

            border-top:
                2px solid #a2763a;

            border-bottom:
                2px solid #a2763a;

            box-shadow:
                0 8px 15px
                rgba(66, 40, 16, 0.24);

            border-radius:
                50% 10px 50% 10px /
                15px 15px 15px 15px;

            overflow: hidden;
        }


        .palm-leaf::before {
            content: "";

            position: absolute;

            inset: 0;

            opacity: 0.30;

            pointer-events: none;

            background:
                repeating-linear-gradient(
                    0deg,
                    transparent 0px,
                    transparent 9px,
                    rgba(92, 60, 26, 0.20) 10px,
                    transparent 11px
                );
        }


        .palm-leaf::after {
            content: "";

            position: absolute;

            left: 18px;
            right: 18px;

            top: 10px;
            bottom: 10px;

            border-top:
                1px solid
                rgba(105, 68, 26, 0.30);

            border-bottom:
                1px solid
                rgba(105, 68, 26, 0.30);

            border-radius: 50%;

            pointer-events: none;
        }


        .leaf-content {
            position: relative;

            z-index: 2;

            width: 100%;
        }


        .kural-text {
            white-space: pre-line;

            font-size: 25px;

            line-height: 1.75;

            font-weight: 600;

            color: #402713;
        }


        .meaning-text {
            white-space: pre-line;

            font-size: 18px;

            line-height: 1.75;

            color: #4d321b;
        }


        .section-label {
            font-size: 14px;

            font-weight: 700;

            letter-spacing: 1px;

            color: #755027;

            margin-bottom: 9px;
        }


        .loading {
            margin-top: 20px;

            color: #765634;

            font-size: 15px;
        }


        /* ================= MOBILE ================= */

        @media (max-width: 650px) {

            .header {
                height: 65px;

                padding:
                    0 15px 0 20px;
            }


            .logo {
                font-size: 21px;
            }


            .logo-icon {
                font-size: 28px;
            }


            .menu-button span {
                width: 30px;
                height: 3px;
            }


            .main {
                padding:
                    40px 15px 60px;
            }


            .search-title {
                font-size: 23px;
            }


            .search-area {
                width: 100%;
                justify-content: center;
            }


            .search-box {
                width: 70vw;

                height: 58px;

                font-size: 17px;
            }


            .search-button {
                width: 58px;
                height: 58px;

                font-size: 21px;
            }


            .palm-leaf {
                width: 96vw;

                padding:
                    25px 30px;
            }


            .kural-text {
                font-size: 19px;

                line-height: 1.7;
            }


            .meaning-text {
                font-size: 15px;

                line-height: 1.65;
            }
        }

    </style>

</head>


<body>


<header class="header">

    <div class="logo">

        <span class="logo-icon">🪶</span>

        <span id="logoText">
            திருக்குறள்
        </span>

    </div>


    <!-- THREE LINES -->

    <button
        class="menu-button"
        id="menuButton"
        type="button">

        <span></span>
        <span></span>
        <span></span>

    </button>


    <!-- LANGUAGE MENU -->

    <div
        class="side-menu"
        id="sideMenu">

        <div
            class="menu-title"
            id="menuTitle">

            மொழி

        </div>


        <button
            class="language-button"
            type="button"
            onclick="changeLanguage('tamil')">

            தமிழ்

        </button>


        <button
            class="language-button"
            type="button"
            onclick="changeLanguage('english')">

            English

        </button>

    </div>

</header>


<main class="main">


    <div
        class="search-title"
        id="searchTitle">

        குறளைத் தேடுக

    </div>


    <div class="search-area">

        <input
            type="number"
            id="kuralNumber"
            class="search-box"
            min="1"
            max="1330"
            placeholder="1 - 1330"
            onkeydown="handleEnter(event)"
        >


        <button
            class="search-button"
            type="button"
            onclick="searchKural()">

            🔍

        </button>

    </div>


    <div
        class="range-text"
        id="rangeText">

        1 முதல் 1330 வரை எண்ணை உள்ளிடவும்

    </div>


    <div
        class="error"
        id="error">
    </div>


    <div id="result"></div>


</main>


<script>


    /* =====================================================
       DEFAULT LANGUAGE
       ===================================================== */

    let currentLanguage = "tamil";


    /* =====================================================
       MENU
       ===================================================== */

    const menuButton =
        document.getElementById("menuButton");

    const sideMenu =
        document.getElementById("sideMenu");


    menuButton.addEventListener(
        "click",
        function(event) {

            event.stopPropagation();

            sideMenu.classList.toggle("active");

        }
    );


    document.addEventListener(
        "click",
        function(event) {

            if (
                !menuButton.contains(event.target) &&
                !sideMenu.contains(event.target)
            ) {

                sideMenu.classList.remove("active");

            }

        }
    );


    /* =====================================================
       CHANGE LANGUAGE
       ===================================================== */

    function changeLanguage(language) {

        currentLanguage = language;

        sideMenu.classList.remove("active");


        if (language === "tamil") {

            document.documentElement.lang = "ta";

            document.title = "திருக்குறள்";

            document.getElementById("logoText")
                .textContent = "திருக்குறள்";

            document.getElementById("menuTitle")
                .textContent = "மொழி";

            document.getElementById("searchTitle")
                .textContent = "குறளைத் தேடுக";

            document.getElementById("rangeText")
                .textContent =
                "1 முதல் 1330 வரை எண்ணை உள்ளிடவும்";

        }

        else {

            document.documentElement.lang = "en";

            document.title = "Thirukkural";

            document.getElementById("logoText")
                .textContent = "Thirukkural";

            document.getElementById("menuTitle")
                .textContent = "Language";

            document.getElementById("searchTitle")
                .textContent = "Search Kural";

            document.getElementById("rangeText")
                .textContent =
                "Enter a number between 1 and 1330";

        }


        const number =
            document.getElementById("kuralNumber").value;


        if (number) {

            searchKural();

        }

    }


    /* =====================================================
       ENTER KEY
       ===================================================== */

    function handleEnter(event) {

        if (event.key === "Enter") {

            searchKural();

        }

    }


    /* =====================================================
       SEARCH KURAL
       ===================================================== */

    async function searchKural() {

        const input =
            document.getElementById("kuralNumber");

        const number =
            parseInt(input.value, 10);

        const error =
            document.getElementById("error");

        const result =
            document.getElementById("result");


        error.textContent = "";

        result.innerHTML = "";


        if (!input.value) {

            return;

        }


        if (
            isNaN(number) ||
            number < 1 ||
            number > 1330
        ) {

            error.textContent =
                currentLanguage === "tamil"
                ? "1 முதல் 1330 வரை உள்ள எண்ணை உள்ளிடவும்."
                : "Please enter a number between 1 and 1330.";

            return;

        }


        result.innerHTML = `
            <div class="loading">
                ${
                    currentLanguage === "tamil"
                    ? "குறள் ஏற்றப்படுகிறது..."
                    : "Loading Kural..."
                }
            </div>
        `;


        try {

            /*
             * IMPORTANT:
             * There is NO extra quote after
             * ${currentLanguage}.
             */

            const response =
                await fetch(
                    `/api/kural/${number}?language=${currentLanguage}`
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Kural not available"
                );

            }


            displayKural(
                number,
                data.kural,
                data.meaning
            );

        }


        catch (err) {

            result.innerHTML = "";

            error.textContent =
                currentLanguage === "tamil"
                ? "குறள் தரவைப் பெற முடியவில்லை."
                : "Unable to get Kural data.";

            console.error(err);

        }

    }


    /* =====================================================
       DISPLAY KURAL
       ===================================================== */

    function displayKural(
        number,
        kural,
        meaning
    ) {

        const result =
            document.getElementById("result");


        const numberText =
            currentLanguage === "tamil"
            ? `குறள் ${number}`
            : `Kural ${number}`;


        const meaningTitle =
            currentLanguage === "tamil"
            ? "பொருள்"
            : "Meaning";


        result.innerHTML = `

            <div class="kural-number">
                ${numberText}
            </div>


            <!-- KURAL PALM LEAF -->

            <div class="palm-leaf">

                <div class="leaf-content">

                    <div class="kural-text">
                        ${escapeHtml(kural)}
                    </div>

                </div>

            </div>


            <!-- MEANING PALM LEAF -->

            <div class="palm-leaf">

                <div class="leaf-content">

                    <div class="section-label">
                        ${meaningTitle}
                    </div>

                    <div class="meaning-text">
                        ${escapeHtml(meaning)}
                    </div>

                </div>

            </div>

        `;

    }


    /* =====================================================
       ESCAPE HTML
       ===================================================== */

    function escapeHtml(text) {

        const div =
            document.createElement("div");

        div.textContent =
            text || "";

        return div.innerHTML;

    }

</script>


</body>

</html>
"""


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template_string(HTML)


# =========================================================
# KURAL API
# =========================================================

@app.route("/api/kural/<int:number>")
def get_kural(number):

    # -----------------------------------------------------
    # CHECK NUMBER
    # -----------------------------------------------------

    if number < 1 or number > 1330:

        return jsonify({
            "error":
            "Kural number must be between 1 and 1330."
        }), 400


    # -----------------------------------------------------
    # GET LANGUAGE
    # -----------------------------------------------------

    language = request.args.get(
        "language",
        "tamil"
    )


    if language not in [
        "tamil",
        "english"
    ]:

        language = "tamil"


    # -----------------------------------------------------
    # KURAL API URL
    # -----------------------------------------------------

    api_url = (
        f"https://tamil-kural-api.vercel.app/api/kural/{number}"
    )


    # -----------------------------------------------------
    # REQUEST API
    # -----------------------------------------------------

    try:

        response = requests.get(
            api_url,
            timeout=20
        )


        print(
            "API STATUS:",
            response.status_code
        )


        print(
            "API RESPONSE:",
            response.text[:500]
        )


        if response.status_code != 200:

            return jsonify({
                "error":
                f"Thirukkural API returned status "
                f"{response.status_code}."
            }), 502


        data = response.json()


    except requests.exceptions.Timeout:

        return jsonify({
            "error":
            "The Kural API took too long to respond."
        }), 504


    except requests.exceptions.ConnectionError:

        return jsonify({
            "error":
            "Python could not connect to the Kural API."
        }), 503


    except ValueError:

        return jsonify({
            "error":
            "The Kural API returned invalid data."
        }), 502


    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error":
            "Unable to read Kural data."
        }), 500


    # -----------------------------------------------------
    # CHECK RESPONSE
    # -----------------------------------------------------

    if not data:

        return jsonify({
            "error":
            "Empty response received from Kural API."
        }), 404


    # -----------------------------------------------------
    # GET KURAL
    # -----------------------------------------------------

    kural_lines = data.get(
        "kural",
        []
    )


    if isinstance(kural_lines, list):

        kural = "\n".join(
            str(line)
            for line in kural_lines
        )

    else:

        kural = str(
            kural_lines
        )


    # -----------------------------------------------------
    # GET MEANING
    # -----------------------------------------------------

    meaning_data = data.get(
        "meaning",
        {}
    )


    if isinstance(meaning_data, dict):

        if language == "tamil":

            meaning = (
                meaning_data.get("ta_mu_va")
                or meaning_data.get("ta")
                or meaning_data.get("tamil")
                or ""
            )

        else:

            meaning = (
                meaning_data.get("en")
                or meaning_data.get("english")
                or ""
            )

    else:

        meaning = str(
            meaning_data
        )


    # -----------------------------------------------------
    # CHECK KURAL
    # -----------------------------------------------------

    if not kural.strip():

        return jsonify({
            "error":
            "Kural was not found."
        }), 404


    # -----------------------------------------------------
    # SEND DATA TO JAVASCRIPT
    # -----------------------------------------------------

    return jsonify({

        "number": number,

        "kural": kural,

        "meaning": meaning

    })


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )