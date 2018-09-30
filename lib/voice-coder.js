'use babel';

import VoiceCoderView from './voice-coder-view';
import { CompositeDisposable } from 'atom';
export default {

  voiceCoderView: null,
  modalPanel: null,
  subscriptions: null,

  activate(state) {
    this.voiceCoderView = new VoiceCoderView(state.voiceCoderViewState);
    this.modalPanel = atom.workspace.addModalPanel({
      item: this.voiceCoderView.getElement(),
      visible: false
    });

    // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    this.subscriptions = new CompositeDisposable();

    // Register command that toggles this view
    this.subscriptions.add(atom.commands.add('atom-workspace', {
      'voice-coder:toggle': () => this.toggle()
    }));

    this.subscriptions.add(atom.commands.add('atom-workspace', {
      'voice-coder:toggleVoiceMode': () => this.toggleVoiceMode()
    }));





    //EDITABLE STUFF FROM HERE ONLY//

    this.editor = atom.workspace.getActiveTextEditor();
    this.voiceMode = false;

    let that = this;
    atom.workspace.onDidChangeActiveTextEditor(function(editor)
  {
      that.editor = editor;
      console.log(editor);
  });



    this.socket = new WebSocket("ws://127.0.0.1:8000/ws/route/");
    this.socket.onopen = function(event)
    {

            console.log(event);

    }

    this.socket.onmessage = function(event)
    {
          console.log(event.data);
          var kaka = JSON.parse(event.data);
          console.log(kaka.type);
          if(that.voiceMode){
          switch(kaka['type'])
          {
            case 'insert':
                {
                  that.editor.insertText(kaka.data);
                  break;
                }
            case 'undo':
              {
                   that.editor.deleteToBeginningOfLine();
                   break;
              }
              case 'snap':
              {
                 that.editor.insertText(kaka.data);
                 that.editor.insertText('\n');
                 break;
              }
            default:
            {
                  console.log('lmao');

            }
          }
         }
    }

  },

  serialize() {
    return {
      voiceCoderViewState: this.voiceCoderView.serialize()
    };
  },

  deactivate() {
    this.modalPanel.destroy();
    this.subscriptions.dispose();
    this.voiceCoderView.destroy();
  },

  toggleVoiceMode()
  {
    this.voiceMode  = !this.voiceMode;
    console.log(this.voiceMode);
  }
  ,
  toggle() {








   console.log(this.socket);
   var b = this.socket;
   //setInterval(function(){b.send(JSON.stringify({'type':'insert', 'data':'textfuckers'}));}, 5000);


  }

};
