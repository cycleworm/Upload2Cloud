using System;
using System.IO;
using WixSharp;

class Script
{
    static public void Main()
    {
        var project = new Project("SendToSkynet",
                          new Dir(@"%ProgramFiles%\\SkynetApplications\\SendToSkynet",
                              //new WixSharp.File("dist\\upload.ico"),
                              //new WixSharp.File("dist\\sendToSkynet.exe"),
                              new WixSharp.Files("dist\\sendToSkynet\\*.*")),
                              //new Dir(@"%Desktop%",
                              new Dir(@"%AppData%/Microsoft/Windows/SendTo",
                                new ExeFileShortcut("- Upload to Skynet", Path.Combine("[INSTALLDIR]", "sendToSkynet.exe"), arguments: "") { WorkingDirectory = "[INSTALLDIR]" })
                              );

        project.GUID = new Guid("6f330b47-2577-43ad-9095-1761ba25889d");
        project.ControlPanelInfo.ProductIcon = "upload.ico";
        project.ControlPanelInfo.Manufacturer = "WiNXuP";

        Compiler.BuildMsi(project);
    }
}