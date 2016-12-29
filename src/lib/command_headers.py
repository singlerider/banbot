import globals

commands = {

}

user_cooldowns = {"channels": {}}


def initalizeCommands(config):
    for channel in config['channels']:
        globals.channel_info[channel.lstrip("#")] = {
            "gamble": {"time": None, "users": {}}}
        user_cooldowns["channels"][channel] = {"commands": {}}
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
            if "user_limit" in commands[command]:
                user_cooldowns["channels"][channel]["commands"][command] = {
                    "users": {}}
