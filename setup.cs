using System;
using WixSharp;

class Script
{
    static public void Main()
    {
        var project = new Project("MyProduct",
                          new Dir(@"%ProgramFiles%\\My Company\\My Product",
                              new File("dist\\upload.ico"),
                              new File("dist\\sendToSkynet.exe")));

    


        project.GUID = new Guid("6f330b47-2577-43ad-9095-1761ba25889d");

        Compiler.BuildMsi(project);
    }
}