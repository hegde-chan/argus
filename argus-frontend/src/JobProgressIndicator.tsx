import {LinearProgress} from "@mui/material";

export function JobProgressIndicator() {
    return (
        <LinearProgress variant="determinate" value={50}/>
    );
}