class activity_DepositAssets():

    def get_no_download_extensions(self, no_download_extensions):
        return [x.strip() for x in no_download_extensions.split(',')]

