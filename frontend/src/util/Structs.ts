export enum Presidents {
  Joe = "joe",
  Donald = "donald",
  Barack = "barack",
}

interface VoiceSegment {
  voice: Presidents;
  file: string;
}
