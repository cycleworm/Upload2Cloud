using System;
using System.IO;
using WixSharp;

class Script
{
    static public void Main()
    {
        var project = new Project("Upload2Cloud",    
                          new Dir(@"%ProgramFiles%\\Upload2Cloud",
                              //new WixSharp.File("dist\\upload.ico"),
                              //new WixSharp.File("dist\\sendToSkynet.exe"),
                              new WixSharp.Files("dist\\Upload2Cloud\\*.*")),

                         

                              //new Dir(@"%Desktop%",
                              new Dir(@"%AppData%/Microsoft/Windows/SendTo",
                                new ExeFileShortcut("- Upload to Skynet", Path.Combine("[INSTALLDIR]", "Upload2Cloud.exe"), arguments: "") { WorkingDirectory = "[INSTALLDIR]" }),
                              new Dir(@"%LocalAppData%/Upload2Cloud",
                                new WixSharp.File("config.json"),
                                new WixSharp.Files("dist\\Webtemplate\\*.*"))
                              );


        project.GUID = new Guid("6f330b47-2577-43ad-9095-1761ba25889d");
        project.MajorUpgradeStrategy = MajorUpgradeStrategy.Default;
        project.MajorUpgradeStrategy.RemoveExistingProductAfter = Step.InstallInitialize;        
        project.ControlPanelInfo.ProductIcon = "upload.ico";
        project.ControlPanelInfo.Manufacturer = "WiNXuP";
        project.LicenceFile = @"Licence.rtf";
        project.Version = new Version("1.0.2"); // for the first setup file
      
        Compiler.BuildMsi(project);
    }
}