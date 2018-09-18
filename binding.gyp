{
	"variables": {
		"ASIO_SDK":"./thirdparty/ASIOSDK2.3"
	},
	"targets": [
		{
			"target_name": "nodeAudioAsio",
			"include_dirs": [
				"<@(ASIO_SDK)/asio",
				"<@(ASIO_SDK)/build",
				"<@(ASIO_SDK)/common",
				"<@(ASIO_SDK)/driver",
				"<@(ASIO_SDK)/host",
				"<@(ASIO_SDK)/host/pc",
				"<!(node -e \"require('nan')\")"
			],
            'conditions': [
              ['OS == "win"', {
                'sources': [
                  # Windows-only; exclude on other platforms.
                  "<@(ASIO_SDK)/host/pc/asiolist.cpp",
    		      "<@(ASIO_SDK)/host/asiodrivers.cpp",
    			  "<@(ASIO_SDK)/common/asio.cpp",
    			  "Source.cpp"
                ]
              }],
            ],
		}
	]
}
