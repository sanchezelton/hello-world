import Pino from 'pino' 
import dayjs from 'dayjs';

const log = Pino ({
    name: "hello-microservices",
    level: "debug",
    prettyPrint: true,
    base: {
        pid: false,
    },
    timestamp: () => `,"time":"${dayjs().format()}"`
});

export default log;