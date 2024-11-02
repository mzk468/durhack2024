import { Cross, Microphone } from "akar-icons"
import { useState } from "react"
import css from "./styles/App.module.css"
import { Presidents } from "./util/Structs"

export default function App() {
    const [whoIsSpeaking, setWhoIsSpeaking] = useState<Presidents | null>(null)
    const [isRecording, setIsRecording] = useState<boolean>(false)

    const handleMicButtonPress = () => {
        if (whoIsSpeaking) setIsRecording(false);
        else setIsRecording(!isRecording);
        if (!isRecording) setWhoIsSpeaking(null);
    }

    return <div id={css.root}>
        {whoIsSpeaking ?
            <img src={`/${whoIsSpeaking}.jpg`} />
            :
            <div id={css.presidentsCont}>
                <img src="/joe.jpg" />
                <img src="/donald.jpg" />
                <img src="/barack.jpg" />
            </div>
        }
        <button id={css.recordButton} onClick={handleMicButtonPress}>
            {isRecording || whoIsSpeaking ? <Cross strokeWidth={3} size={48} color="white" /> : <Microphone strokeWidth={3} size={48} color="white" />}
        </button>
    </div>
}
