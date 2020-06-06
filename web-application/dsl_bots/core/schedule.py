import datetime
import sched
import time


class Schedule:
    def __init__(self, schedule_date_time_parameters, action, api, account, campaign):
        self.schedule_date_time_parameters = schedule_date_time_parameters
        self.action = action
        self.tweepy_api = api
        self.account = account
        self.campaign = campaign

    def schedule(self):
        scheduler = sched.scheduler(time.time, time.sleep)
        date_time_schedule = datetime.datetime(2020, int(self.schedule_date_time_parameters.get('month')), int(self.schedule_date_time_parameters.get('day_of_month')),
                                               int(self.schedule_date_time_parameters.get('hour')), int(self.schedule_date_time_parameters.get('minute')))
        time_delay_seconds = (date_time_schedule - datetime.datetime.now()).total_seconds()
        scheduler.enterabs(time.time() + time_delay_seconds, 1, self.execute, argument=(self.action,))
        scheduler.run()

    def execute(self, input_statement):
        from core.execute import Execute
        execute = Execute(account=self.account, campaign=self.campaign)
        parser = execute.build_lexer_parser(input_statement=input_statement)
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree, api=self.tweepy_api)
