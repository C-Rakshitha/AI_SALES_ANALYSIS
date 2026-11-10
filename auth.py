
import streamlit as st


def google_login():

    if not st.user.is_logged_in:

        st.html("""
        <style>

        /* PAGE BACKGROUND */
        .stApp {
            background: linear-gradient(
                135deg,
                #d8c5ff,
                #f8f6ff,
                #cbb8ff
            );
        }

        /* IMPORTANT: KEEP CONTENT BELOW THE TOP TOOLBAR */
        .block-container {
            max-width: 1000px !important;
            padding-top: 3.5rem !important;
            padding-bottom: 2rem !important;
        }

        /* MAIN TITLE */
        .login-title {
            display: block;
            width: 100%;
            text-align: center;
            font-size: 42px;
            line-height: 1.4;
            font-weight: 800;
            color: #292477;
            padding-top: 15px;
            margin: 0 auto 8px auto;
            overflow: visible;
        }

        .login-subtitle {
            text-align: center;
            font-size: 18px;
            line-height: 1.5;
            color: #29345f;
            margin: 0 auto 12px auto;
        }

        .login-line {
            width: 130px;
            height: 6px;
            border-radius: 10px;
            background: linear-gradient(
                90deg,
                #a855f7,
                #3b82f6
            );
            margin: 15px auto 22px auto;
        }

        /* LOGIN CARD */
        .login-card {
            background: rgba(255,255,255,0.95);
            border: 1px solid white;
            border-radius: 35px;
            padding: 25px 35px;
            width: 100%;
            max-width: 780px;
            margin: 0 auto;
            text-align: center;
            box-shadow: 0 20px 55px rgba(89,57,180,0.18);
            box-sizing: border-box;
        }

        /* ILLUSTRATION */
        .illustration {
            min-height: 145px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-bottom: 10px;
        }

        .plant,
        .coffee {
            font-size: 45px;
        }

        .laptop {
            width: 250px;
            height: 135px;
            background: #292477;
            border: 7px solid #292477;
            border-radius: 15px;
            padding: 6px;
            box-shadow: 0 10px 20px #c4b5fd;
            box-sizing: border-box;
        }

        .screen {
            background: #f4f0ff;
            height: 100%;
            border-radius: 8px;
            padding: 9px;
            box-sizing: border-box;
        }

        .screen-dots {
            text-align: left;
            color: #8b5cf6;
            font-size: 11px;
        }

        .chart-area {
            height: 75px;
            display: flex;
            align-items: end;
            justify-content: center;
            gap: 12px;
            border-bottom: 2px solid #c4b5fd;
        }

        .chart-bar {
            width: 20px;
            border-radius: 5px 5px 0 0;
            background: linear-gradient(
                #a855f7,
                #3b82f6
            );
        }

        .bar1 { height: 25px; }
        .bar2 { height: 40px; }
        .bar3 { height: 55px; }
        .bar4 { height: 70px; }

        /* GOOGLE LOGO */
        .google-circle {
            width: 75px;
            height: 75px;
            background: white;
            border-radius: 50%;
            margin: 15px auto;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 8px 20px #d8d4ef;
        }

        .google-circle img {
            width: 50px;
            height: 50px;
        }

        /* WELCOME TEXT */
        .welcome-heading {
            font-size: 37px;
            line-height: 1.3;
            font-weight: 800;
            color: #101b50;
            margin: 8px 0;
        }

        .welcome-subtitle {
            font-size: 18px;
            line-height: 1.5;
            color: #39446c;
            margin-bottom: 8px;
        }

        /* GOOGLE LOGIN BUTTON */
        div.stButton > button {
            background: linear-gradient(
                100deg,
                #1689e8,
                #7900ed
            ) !important;
            color: white !important;
            border: none !important;
            border-radius: 18px !important;
            height: 52px !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            box-shadow: 0 10px 20px rgba(80,50,180,0.2);
        }

        div.stButton > button:hover {
            opacity: 0.9;
            border: none !important;
        }

        /* SECURITY MESSAGE */
        .secure-text {
            width: 100%;
            text-align: center;
            font-size: 16px;
            color: #39446c;
            margin: 12px auto;
            padding-bottom: 15px;
        }

        /* MOBILE SCREEN */
        @media (max-width: 600px) {

            .block-container {
                padding-top: 2rem !important;
            }

            .login-title {
                font-size: 29px;
                padding-top: 10px;
            }

            .login-subtitle {
                font-size: 15px;
            }

            .login-card {
                padding: 18px 10px;
                border-radius: 24px;
            }

            .illustration {
                gap: 5px;
                min-height: 115px;
            }

            .plant,
            .coffee {
                font-size: 28px;
            }

            .laptop {
                transform: scale(0.75);
            }

            .welcome-heading {
                font-size: 28px;
            }

            .welcome-subtitle {
                font-size: 15px;
            }

        }

        </style>

        <div class="login-title">
            📊 AI Sales Analytics
        </div>

        <div class="login-subtitle">
            Welcome! Sign in to continue to your dashboard.
        </div>

        <div class="login-line"></div>

        <div class="login-card">

            <div class="illustration">

                <div class="plant">🪴</div>

                <div class="laptop">

                    <div class="screen">

                        <div class="screen-dots">
                            ● &nbsp; ● &nbsp; ●
                        </div>

                        <div class="chart-area">
                            <div class="chart-bar bar1"></div>
                            <div class="chart-bar bar2"></div>
                            <div class="chart-bar bar3"></div>
                            <div class="chart-bar bar4"></div>
                        </div>

                    </div>

                </div>

                <div class="coffee">☕</div>

            </div>

            <div class="google-circle">

                <img
                    src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
                    alt="Google Logo"
                />

            </div>

            <div class="welcome-heading">
                Welcome Back!
            </div>

            <div class="welcome-subtitle">
                Login using your Google account
            </div>

        </div>
        """)

        # GOOGLE LOGIN BUTTON
        left, center, right = st.columns([1, 2, 1])

        with center:

            st.button(
                "🌐 Login with Google",
                on_click=st.login,
                type="primary",
                use_container_width=True
            )

        # SECURITY MESSAGE
        st.html("""
        <div class="secure-text">
            🔒 Secure authentication powered by Google
        </div>
        """)

        st.stop()

    # LOGGED-IN USER
    return
