from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import webbrowser

class FfExtension(Extension): 

 
    def __init__(self):
        super(FfExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

   

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        items = [
            ExtensionResultItem(
                icon = 'images/firefox.svg',
                name = event.get_argument(),
                description = 'Open %s in firefox' % event.get_argument(),
                on_enter=ExtensionCustomAction(query, keep_app_open=True)
            )
        ]



        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_data() or str()
        webbrowser.open_new_tab('https://' + query)

        return RenderResultListAction([])

if __name__ == '__main__':
    FfExtension().run()