import {Component} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'adilet-capstone-web';
  message: string = null;

  simpleImg: any = null;
  simpleImgFile: File = null;

  heatImg: any = null;
  heatImgFile: any = null;

  heatHotImgOutput: any = null;
  heatIrImgOutput: any = null;
  classes = null;

  constructor(private http: HttpClient) {
  }

  previewHeatImage(event) {
    const fileList: FileList = event.target.files;
    if (fileList.length === 0) {
      return;
    }
    const mimeType = fileList[0].type;
    if (mimeType.match(/image\/*/) == null) {
      this.message = "Only images are supported.";
      return;
    }
    const reader = new FileReader();
    // this.imagePath = files;
    reader.onload = (_event) => {
      this.heatImg = reader.result;
    }
    reader.readAsDataURL(fileList[0]);
    this.heatImgFile = fileList[0];
  }

  previewSimpleImage(event) {
    const fileList: FileList = event.target.files;
    if (fileList.length === 0) {
      return;
    }
    const mimeType = fileList[0].type;
    if (mimeType.match(/image\/*/) == null) {
      this.message = "Only images are supported.";
      return;
    }
    const reader = new FileReader();
    // this.imagePath = files;
    reader.onload = (_event) => {
      this.simpleImg = reader.result;
    }
    reader.readAsDataURL(fileList[0]);
    this.simpleImgFile = fileList[0];
  }

  uploadHeatImage() {
    if (!this.heatImgFile) {
      return;
    }

    const formData: FormData = new FormData();
    formData.append('uploadFile', this.heatImgFile, this.heatImgFile.name);
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Accept', 'image/jpg');

    this.http.post('/api/heat-hot-image', formData, {headers: headers, responseType: 'blob'},).subscribe(res => {
        console.log(res);
        this.showHeatHotImgOutput(res);
      }
    )
    this.http.post('/api/heat-ir-image', formData, {headers: headers, responseType: 'blob'},).subscribe(res => {
        console.log(res);
        this.showHeatIrImgOutput(res);
      }
    )
  }


  uploadSimpleImage() {
    if (!this.simpleImgFile) {
      return;
    }

    const formData: FormData = new FormData();
    formData.append('uploadFile', this.simpleImgFile, this.simpleImgFile.name);
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Accept', 'image/jpg');
    this.http.post('/api/simple-image', formData, {headers: headers}).subscribe(res => {
        console.log(res);
        this.classes = res;
      }
    )
  }

  showHeatHotImgOutput(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.heatHotImgOutput = reader.result;
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  showHeatIrImgOutput(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.heatIrImgOutput = reader.result;
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

}
