import json

def dump(fname, data):
	with open(fname, 'w') as f:
		json.dump(data, f, indent=4)


REPOS = {
	"42_common_core": {
		'langs': '',
		'frames_and_libs': '',
	},
	"42_Exams": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"Born2beroot": {
		'langs': 'Bash',
		'frames_and_libs': '',
	},
	"CPP": {
		'langs': 'C++',
		'frames_and_libs': '',
	},
	"cube3d": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"DAAB_Piscine": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"ft_containers": {
		'langs': 'C++',
		'frames_and_libs': '',
	},
	"ft_printf": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"get_next_line": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"Libft": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"minishell": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"minitalk": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"net_practice": {
		'langs': '',
		'frames_and_libs': '',
	},
	"philosophers": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"Piscine": {
		'langs': 'Bash C',
		'frames_and_libs': '',
	},
	"push_swap": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"so_long": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"biped_bot": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"simple_alarm": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"sunflower_1_LDR": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"sunflower_2_LDR": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"sunflower_4_LDR": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"werable_health_tracker": {
		'langs': 'Arduino',
		'frames_and_libs': '',
	},
	"face_detection": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},
	"face_mesh": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},
	"finger_counter": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},
	"Hand_Tracking": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},
	"personal_ai_trainer": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},
	"pose_estimation": {
		'langs': 'Python',
		'frames_and_libs': 'OpenCV',
	},









	"analyzing_cryptocurrencies": {
		'langs': 'Python',
		'frames_and_libs': 'Pandas Matplotlib',
	},
	"bitcoin_daily_return": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib',
	},
	"bitcoin_prediction_ML": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas',
	},
	"bitcoin_prediction_NN": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib Scikit_Learn TensorFlow Keras',
	},
	"bitcoin_price_prediction": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib Scikit_Learn Keras',
	},
	"bitcoin_twitter_sentiment_analysis": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib',
	},
	"channels_detection": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib',
	},
	"equal_weight_s_p_500_index_fund": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas',
	},
	"fake_news_detection": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Scikit_Learn',
	},
	"fake_news_detection_4_models": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Scikit_Learn',
	},
	"head_and_shoulders_detection": {
		'langs': 'Python',
		'frames_and_libs': 'Pandas Numpy',
	},
	"price_prediction_chain": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib Scikit_Learn Keras',
	},
	"quantitative_momentum_investing_strategy": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas',
	},
	"quantitative_value_investing_strategy": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas',
	},
	"triangle_detection": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas',
	},
	"twitter_bitcoin_sentiment_analysis": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Pandas Matplotlib Scikit_Learn',
	},







	"game_1": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"game_2": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"game_3": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"game_4": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"game_5": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"game_6": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"visual_novel": {
		'langs': 'Python',
		'frames_and_libs': 'Ren_py',
	},





	"auto_hot_key_win": {
		'langs': 'Auto_Hot_Key',
		'frames_and_libs': '',
	},
	"C_learn": {
		'langs': 'C',
		'frames_and_libs': '',
	},
	"drive_auto_backup": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"file_converter": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"Houseki": {
		'langs': 'Python',
		'frames_and_libs': 'Kivy KivyMD',
	},
	"nyquist_visualizer": {
		'langs': 'Python',
		'frames_and_libs': 'Matplotlib',
	},
	"os-dev": {
		'langs': 'Assembly C',
		'frames_and_libs': '',
	},
	"python_builder": {
		'langs': 'Python',
		'frames_and_libs': 'Pyinstaller',
	},
	"telegram_bot_sample": {
		'langs': 'Python',
		'frames_and_libs': '',
	},






	"opengl_python": {
		'langs': 'Python',
		'frames_and_libs': 'OpenGL',
	},






	"connect_four": {
		'langs': 'Java',
		'frames_and_libs': '',
	},
	"HW2": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"HW4": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"HW6": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"HW8": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"introduction_to_algorithms": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"roman_scraper": {
		'langs': 'Java',
		'frames_and_libs': '',
	},




	"badge_generator": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"controller_tester": {
		'langs': 'Python',
		'frames_and_libs': 'Pygame',
	},
	"kivymd_style": {
		'langs': 'Python',
		'frames_and_libs': 'Kivy KivyMD',
	},
	"pip_upgrader": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"repo_maintainer": {
		'langs': 'Python',
		'frames_and_libs': '',
	},
	"wave_reader": {
		'langs': 'Python',
		'frames_and_libs': 'Numpy Matplotlib',
	},
}

for repo in REPOS:
	REPOS[repo]['langs'] = REPOS[repo]['langs'].split(' ')
	REPOS[repo]['frames_and_libs'] = REPOS[repo]['frames_and_libs'].split(' ')
	if REPOS[repo]['langs'][0] == '':
		REPOS[repo].pop('langs')
	if REPOS[repo]['frames_and_libs'][0] == '':
		REPOS[repo].pop('frames_and_libs')


dump('test.json', REPOS)