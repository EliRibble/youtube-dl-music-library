"Logic for installing the module."
import setuptools # type: ignore

setuptools.setup(
	install_requires=[
		"youtube_dl",
	],
	extras_require={
		"develop": [
			"mypy",
			"nose2",
			"pylint",
		]
	},
)
