import * as fs from 'fs';

export function readLinesAsNumbers(filePath: string): number[] {
    const lines = fs.readFileSync(filePath, 'utf8').split(',');
    return lines.map(Number);
}

