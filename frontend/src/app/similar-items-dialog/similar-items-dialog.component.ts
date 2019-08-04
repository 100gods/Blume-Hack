import {Component, Inject} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import * as _ from 'lodash';

@Component({
    selector: 'app-similar-items-dialog',
    templateUrl: './similar-items-dialog.component.html',
    styleUrls: ['./similar-items-dialog.component.css']
})
export class SimilarItemsDialogComponent {
    constructor(
        public dialogRef: MatDialogRef<SimilarItemsDialogComponent>,
        @Inject(MAT_DIALOG_DATA) public data) {
        console.log("dialog data : ", data.data.docs);
        _.each(data.data.docs, d => {
            d.description = d.description[0].substr(2, d.description[0].indexOf("',") - 3).replace(/\\u2022/g, '');
            ;
        })

    }

    ngOnInit() {
    }


}
